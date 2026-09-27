#!/usr/bin/env python3
"""Render cv-v7-base.md -> DOCX + PDF.

Strict parser for the source grammar documented in job-hunt/render_cv.md.
Dependencies: reportlab. pypdf only for the optional self-check.
"""
import re, html, sys, os, zipfile

BASE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(BASE, "cv", "cv-v7-base.md")
STEM = os.path.join(BASE, "cv", "Samuel_Couchman_CV_v7")

# ---------------------------------------------------------------- parsing

def parse(src):
    """-> (header_lines, sections) where sections = [(heading, [blocks])].
    block kinds: ('job', role, meta, context, bullets) | ('cat', label, tools)
                 | ('bullet', text) | ('para', text) | ('italic', text)"""
    header = []
    sections = []
    cur = None
    for raw in src.split('\n'):
        line = raw.rstrip()
        if not line.strip() or line.strip() == '---':
            continue
        if line.startswith('## '):
            cur = [line[3:].strip(), []]
            sections.append(cur)
            continue
        target = header if cur is None else cur[1]
        target.append(line)
    return header, [(h, l) for h, l in sections]


def plain(s):
    """markdown -> plain text (strips ** and *)"""
    s = re.sub(r'\*\*(.+?)\*\*', r'\1', s)
    s = re.sub(r'\*(.+?)\*', r'\1', s)
    return s.strip()


def header_lines(header):
    """Name / tagline / contact / eligibility from the pre-heading block."""
    h = [plain(x).lstrip('# ').strip() for x in header]
    name = h[0] if h else 'SAMUEL-ALEXANDER COUCHMAN'
    tagline = h[1] if len(h) > 1 else ''
    contact = next((x for x in h[2:] if '@' in x), '')
    elig = next((x for x in h[2:] if 'citizenship' in x.lower() or 'authorized' in x.lower()), '')
    return name, tagline, contact, elig


def section_blocks(lines):
    """Turn a section's raw lines into typed blocks."""
    blocks, i = [], 0
    while i < len(lines):
        line = lines[i]
        s = line.strip()
        if not s:
            i += 1
            continue
        if s.startswith('- ') or s.startswith('* '):
            bullets = []
            while i < len(lines) and (lines[i].strip().startswith('- ') or lines[i].strip().startswith('* ')):
                bullets.append(plain(lines[i].strip()[2:]))
                i += 1
            blocks.append(('bullets', bullets))
            continue
        if s.startswith('|'):
            # markdown table: drop separator rows, drop the header row, emit date|value pairs
            rows = [r for r in lines[i:] if r.strip() and not set(r.strip()) <= set('|-: ')]
            cells0 = [c.strip() for c in rows[0].strip().strip('|').split('|')] if rows else []
            for r in rows[1:] if len(cells0) == 2 and cells0[0] in ('Date', 'Language') else rows:
                c = [x.strip() for x in r.strip().strip('|').split('|')]
                blocks.append(('pair', ' — '.join(c)))
            break
        if s.startswith('**') and s.endswith('**') and i + 1 < len(lines):
            # category heading: label line, tools on the NEXT line
            label = plain(s)
            nxt = lines[i + 1].strip()
            if nxt and not nxt.startswith('- '):
                blocks.append(('cat', label, plain(nxt)))
                i += 2
                continue
        if s.startswith('**') and ' | ' in s:
            # job header: **Role** | Employer · Dates · Location
            parts = s.split(' | ', 1)
            role = plain(parts[0])
            rest = plain(parts[1]) if len(parts) > 1 else ''
            context, bullets = '', []
            j = i + 1
            if j < len(lines) and lines[j].strip().startswith('*') and not lines[j].strip().startswith('- '):
                context = plain(lines[j].strip())
                j += 1
            while j < len(lines) and (lines[j].strip().startswith('- ') or lines[j].strip().startswith('* ')):
                bullets.append(plain(lines[j].strip()[2:]))
                j += 1
            blocks.append(('job', role, rest, context, bullets))
            i = j
            continue
        blocks.append(('para', plain(s)))
        i += 1
    return blocks


# ---------------------------------------------------------------- docx

def esc(t):
    return html.escape(t)


def docx_runs(text, sz=None, bold=False, italic=False):
    rpr = ''
    if bold: rpr += '<w:b/>'
    if italic: rpr += '<w:i/>'
    if sz: rpr += f'<w:sz w:val="{sz}"/>'
    rpr = f'<w:rPr>{rpr}</w:rPr>' if rpr else ''
    return f'<w:r>{rpr}<w:t xml:space="preserve">{esc(text)}</w:t></w:r>'


def dpara(text, sz=20, bold=False, italic=False, before=0, after=60, ind=None, jc=None,
          rule=False, color=None, keep_next=False):
    ppr = f'<w:pPr><w:spacing w:before="{before}" w:after="{after}"/>'
    if keep_next: ppr += '<w:keepNext/><w:keepLines/>'
    if ind: ppr += f'<w:ind w:left="{ind}" w:hanging="200"/>'
    if jc: ppr += f'<w:jc w:val="{jc}"/>'
    if rule: ppr += '<w:pBdr><w:bottom w:val="single" w:sz="6" w:space="1" w:color="999999"/></w:pBdr>'
    ppr += '</w:pPr>'
    return f'<w:p>{ppr}{docx_runs(text, sz, bold, italic)}</w:p>'


def build_docx(name, tagline, contact, elig, sections, out):
    body: list = [dpara(name, sz=40, bold=True, after=20, jc='center'),
            dpara(tagline, sz=19, after=20, jc='center'),
            dpara(contact, sz=18, after=20, jc='center'),
            dpara(elig, sz=18, bold=True, after=40, jc='center')]
    for heading, lines in sections:
        body.append(dpara(heading, sz=23, bold=True, before=200, after=80, rule=True))
        for b in section_blocks(lines):
            k = b[0]
            if k == 'bullets':
                for t in b[1]:
                    body.append(dpara('•  ' + t, ind=300, after=25))
            elif k == 'pair':
                body.append(dpara('•  ' + b[1], ind=300, after=25))
            elif k == 'cat':
                ppr = ('<w:pPr><w:spacing w:before="50" w:after="45"/>'
                       '<w:keepNext/><w:keepLines/></w:pPr>')
                runs = (docx_runs(b[1] + ': ', bold=True)
                        + docx_runs(b[2]))
                body.append(f'<w:p>{ppr}{runs}</w:p>')
            elif k == 'job':
                _, role, rest, context, bullets = b
                body.append(dpara(role + ' | ' + rest, bold=True, before=60, after=10,
                                  keep_next=True))
                if context:
                    body.append(dpara(context, sz=17, italic=True, after=25))
                for t in bullets:
                    body.append(dpara('•  ' + t, ind=300, after=25))
            else:
                body.append(dpara(b[1], after=70))
    sect = ('<w:sectPr><w:pgSz w:w="11906" w:h="16838"/>'
            '<w:pgMar w:top="1000" w:right="1050" w:bottom="1000" w:left="1050"/></w:sectPr>')
    doc = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
           '<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">'
           f'<w:body>{"".join(body)}{sect}</w:body></w:document>')
    styles = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
              '<w:styles xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">'
              '<w:docDefaults><w:rPrDefault><w:rPr>'
              '<w:rFonts w:ascii="Calibri" w:hAnsi="Calibri" w:cs="Calibri"/><w:sz w:val="20"/>'
              '</w:rPr></w:rPrDefault><w:pPrDefault><w:pPr>'
              '<w:spacing w:after="60" w:line="240" w:lineRule="auto"/></w:pPr></w:pPrDefault>'
              '</w:docDefaults><w:style w:type="paragraph" w:default="1" w:styleId="Normal">'
              '<w:name w:val="Normal"/><w:qFormat/></w:style></w:styles>')
    ct = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
          '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
          '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>'
          '<Default Extension="xml" ContentType="application/xml"/>'
          '<Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>'
          '<Override PartName="/word/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/>'
          '</Types>')
    rels = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
            '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
            '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>'
            '</Relationships>')
    drels = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
             '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
             '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/>'
             '</Relationships>')
    z = zipfile.ZipFile(out, 'w', zipfile.ZIP_DEFLATED)
    z.writestr('[Content_Types].xml', ct)
    z.writestr('_rels/.rels', rels)
    z.writestr('word/document.xml', doc)
    z.writestr('word/_rels/document.xml.rels', drels)
    z.writestr('word/styles.xml', styles)
    z.close()


# ---------------------------------------------------------------- pdf

def build_pdf(name, tagline, contact, elig, sections, out):
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.styles import ParagraphStyle
    from reportlab.lib.units import mm
    from reportlab.lib import colors
    from reportlab.platypus import (SimpleDocTemplate, Paragraph, HRFlowable,
                                    KeepTogether, CondPageBreak)
    from reportlab.lib.enums import TA_CENTER

    S = lambda **k: ParagraphStyle('s', **k)
    NAME = S(fontName='Helvetica-Bold', fontSize=19, leading=22, spaceAfter=3, alignment=TA_CENTER)
    TAG = S(fontName='Helvetica', fontSize=10, leading=12.5, spaceAfter=2, alignment=TA_CENTER)
    CON = S(fontName='Helvetica', fontSize=9.3, leading=11.8, spaceAfter=2, alignment=TA_CENTER)
    ELIG = S(fontName='Helvetica-Bold', fontSize=9.3, leading=11.8, spaceAfter=5, alignment=TA_CENTER)
    HEAD = S(fontName='Helvetica-Bold', fontSize=11, leading=12.6, spaceBefore=8, spaceAfter=3)
    JOB = S(fontName='Helvetica-Bold', fontSize=9.6, leading=12.2, spaceBefore=5, spaceAfter=1)
    ITAL = S(fontName='Helvetica-Oblique', fontSize=8.6, leading=10.4, spaceAfter=3,
             textColor=colors.HexColor('#555555'))
    BODY = S(fontName='Helvetica', fontSize=9.1, leading=12.0, spaceAfter=4)
    BULT = S(fontName='Helvetica', fontSize=9.1, leading=12.0, leftIndent=11, firstLineIndent=-8, spaceAfter=1.6)
    CAT = S(fontName='Helvetica-Bold', fontSize=8.9, leading=10.8, spaceBefore=2.5, spaceAfter=0.5)
    TOOL = S(fontName='Helvetica', fontSize=8.9, leading=11.0, spaceAfter=2)
    CATLINE = S(fontName='Helvetica', fontSize=9.4, leading=12.4, spaceBefore=4.5, spaceAfter=3.5,
                leftIndent=9, firstLineIndent=-9)

    def E(t):
        t = html.escape(t)
        return re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', re.sub(r'\*(.+?)\*', r'<i>\1</i>', t))

    flow: list = [Paragraph(E(name), NAME), Paragraph(E(tagline), TAG),
                 Paragraph(E(contact), CON), Paragraph(E(elig), ELIG)]
    # Sections that must not begin near the foot of a page: breaking mid-section
    # orphaned the first category label from its tool list.
    NO_SPLIT = {'TECHNICAL SKILLS', 'CERTIFICATIONS', 'LANGUAGES'}
    for heading, lines in sections:
        if heading.strip().upper() in NO_SPLIT:
            flow.append(CondPageBreak(38 * mm))
        flow.append(Paragraph(E(heading), HEAD))
        flow.append(HRFlowable(width='100%', thickness=0.4,
                               color=colors.HexColor('#999999'), spaceBefore=0, spaceAfter=4))
        for b in section_blocks(lines):
            k = b[0]
            if k == 'bullets':
                for t in b[1]:
                    flow.append(Paragraph('•  ' + E(t), BULT))
            elif k == 'pair':
                flow.append(Paragraph('\u2022  ' + E(b[1]), BULT))
            elif k == 'cat':
                flow.append(KeepTogether([
                    Paragraph('<b>' + E(b[1]) + ':</b> ' + E(b[2]), CATLINE)]))
            elif k == 'job':
                _, role, rest, context, bullets = b
                # header+context kept together; bullets may flow. Keeping the WHOLE
                # entry together pushed the CV to 3 pages — too coarse.
                grp = [Paragraph(E(role + ' | ' + rest), JOB)]
                if context:
                    grp.append(Paragraph(E(context), ITAL))
                # require room for header + context, else push the entry to the next page
                flow.append(CondPageBreak(20 * mm))
                flow.append(KeepTogether(grp))
                for t in bullets:
                    flow.append(Paragraph('•  ' + E(t), BULT))
            else:
                flow.append(Paragraph(E(b[1]), BODY))

    SimpleDocTemplate(out, pagesize=A4, leftMargin=17 * mm, rightMargin=17 * mm,
                      topMargin=14 * mm, bottomMargin=14 * mm,
                      title=f'{name} — CV', author=name).build(flow)


# ---------------------------------------------------------------- main

if __name__ == '__main__':
    src = open(SRC).read()
    header, sections = parse(src)
    name, tagline, contact, elig = header_lines(header)
    docx = STEM + '.docx'
    pdf = STEM + '.pdf'
    build_docx(name, tagline, contact, elig, sections, docx)
    build_pdf(name, tagline, contact, elig, sections, pdf)
    print('wrote', docx)
    print('wrote', pdf)
