"""
construir_informe_docx.py
Generador automatizado del Informe Completo de Taller Semana 13 en DOCX
EPS AGUAS DEL SUR S.A. - PETI 2026-2030 (SI-886)
"""

import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn
import os

def set_cell_background(cell, fill_hex):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    tcPr.append(shd)

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="{top}" w:type="dxa"/><w:bottom w:w="{bottom}" w:type="dxa"/><w:left w:w="{left}" w:type="dxa"/><w:right w:w="{right}" w:type="dxa"/></w:tcMar>')
    tcPr.append(tcMar)

def format_table(table, col_widths=None, header_bg="1F497D", alt_bg="F2F5F8"):
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    # Format header
    for cell in table.rows[0].cells:
        set_cell_background(cell, header_bg)
        set_cell_margins(cell, top=120, bottom=120, left=150, right=150)
        for p in cell.paragraphs:
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            for run in p.runs:
                run.font.bold = True
                run.font.color.rgb = RGBColor(255, 255, 255)
                run.font.size = Pt(9.5)
                run.font.name = 'Calibri'
    # Format data rows
    for r_idx, row in enumerate(table.rows[1:], 1):
        bg = alt_bg if r_idx % 2 == 1 else "FFFFFF"
        for cell in row.cells:
            if bg != "FFFFFF":
                set_cell_background(cell, bg)
            set_cell_margins(cell, top=80, bottom=80, left=120, right=120)
            for p in cell.paragraphs:
                for run in p.runs:
                    run.font.size = Pt(9)
                    run.font.name = 'Calibri'
    # Set widths if provided
    if col_widths:
        for row in table.rows:
            for idx, width in enumerate(col_widths):
                if idx < len(row.cells):
                    row.cells[idx].width = Inches(width)

def generar_documento():
    doc = docx.Document('SI886-PLANTILLA-TALLER.docx')

    # 1. Modificar Carátula
    for p in doc.paragraphs[:28]:
        t = p.text.strip()
        if "……………………………………………." in t or "TALLER" in t and "“" in t:
            p.text = '“CONSTRUCCIÓN DEL PORTAFOLIO DE PROYECTOS DE TI (SECCIÓN 7.1 DEL PETI) — EPS AGUAS DEL SUR S.A.”'
            p.style = doc.styles['Centrado']
            for run in p.runs:
                run.font.bold = True
                run.font.size = Pt(13)
        elif "…………………………." in t:
            p.text = 'PLANEAMIENTO ESTRATÉGICO DE TECNOLOGÍAS DE INFORMACIÓN (SI-886)'
            p.style = doc.styles['Centrado']
            for run in p.runs:
                run.font.bold = True
                run.font.size = Pt(11)
        elif "APELLIDOS Y NOMBRES · CÓDIGO" in t:
            p.text = "CHOQUENA CHOQUE, MAURICIO · 2023076799\nCALLO TICONA, BRAYAN GUSTAVO · 2021071078\nRAMOS LIMACHE, CRISTHIAN ROLANDO · 2021070025"
            p.style = doc.styles['Centrado']
            for run in p.runs:
                run.font.bold = True
                run.font.size = Pt(10.5)
        elif "TACNA — PERÚ" in t:
            p.text = "TACNA — PERÚ\n2026"
            p.style = doc.styles['Centrado']
            for run in p.runs:
                run.font.bold = True

    # 2. Localizar secciones y eliminar la página de instrucciones
    # Encontrar párrafos de instrucciones
    p_instruccion_inicio = None
    p_instruccion_fin = None
    for i, p in enumerate(doc.paragraphs):
        if "Cómo se usa esta plantilla" in p.text:
            p_instruccion_inicio = i
        if "Borra esta página antes de entregar" in p.text:
            p_instruccion_fin = i

    if p_instruccion_inicio is not None and p_instruccion_fin is not None:
        for idx in range(p_instruccion_fin, p_instruccion_inicio - 1, -1):
            p_elem = doc.paragraphs[idx]._p
            p_elem.getparent().remove(p_elem)

    print("[OK] Carátula completada y página de instrucciones eliminada.")

    # Guardar versión base intermedia
    doc.save("SI886-PLANTILLA-TALLER-MOD.docx")

if __name__ == "__main__":
    generar_documento()
