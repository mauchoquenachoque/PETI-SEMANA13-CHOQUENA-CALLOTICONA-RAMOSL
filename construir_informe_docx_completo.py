"""
construir_informe_docx_completo.py
Construye el informe completo y profesional de la Semana 13 sobre la plantilla DOCX.
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

def set_cell_margins(cell, top=100, bottom=100, left=140, right=140):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="{top}" w:type="dxa"/><w:bottom w:w="{bottom}" w:type="dxa"/><w:left w:w="{left}" w:type="dxa"/><w:right w:w="{right}" w:type="dxa"/></w:tcMar>')
    tcPr.append(tcMar)

def style_table(table, col_widths, header_bg="1B365D", alt_bg="F0F4F8"):
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    # Header row
    for idx, cell in enumerate(table.rows[0].cells):
        set_cell_background(cell, header_bg)
        set_cell_margins(cell, top=120, bottom=120, left=140, right=140)
        cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
        for p in cell.paragraphs:
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            for run in p.runs:
                run.font.bold = True
                run.font.color.rgb = RGBColor(255, 255, 255)
                run.font.size = Pt(9)
                run.font.name = 'Calibri'
    # Data rows
    for r_idx, row in enumerate(table.rows[1:], 1):
        bg = alt_bg if r_idx % 2 == 1 else "FFFFFF"
        for idx, cell in enumerate(row.cells):
            if bg != "FFFFFF":
                set_cell_background(cell, bg)
            set_cell_margins(cell, top=80, bottom=80, left=120, right=120)
            cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
            for p in cell.paragraphs:
                for run in p.runs:
                    run.font.size = Pt(8.5)
                    run.font.name = 'Calibri'
    # Widths
    for row in table.rows:
        for idx, width in enumerate(col_widths):
            if idx < len(row.cells):
                row.cells[idx].width = Inches(width)

def add_callout(doc, text, title="NOTA TÉCNICA"):
    tbl = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = tbl.cell(0, 0)
    set_cell_background(cell, "EBF3FB")
    set_cell_margins(cell, top=120, bottom=120, left=180, right=180)
    # Left border highlight
    tcPr = cell._tc.get_or_add_tcPr()
    tcBorders = parse_xml(f'<w:tcBorders {nsdecls("w")}><w:left w:val="single" w:sz="24" w:space="0" w:color="1B365D"/><w:top w:val="none"/><w:right w:val="none"/><w:bottom w:val="none"/></w:tcBorders>')
    tcPr.append(tcBorders)
    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(2)
    p.paragraph_format.space_after = Pt(2)
    r1 = p.add_run(f"{title}: ")
    r1.font.bold = True
    r1.font.color.rgb = RGBColor(27, 54, 93)
    r1.font.size = Pt(9.5)
    r2 = p.add_run(text)
    r2.font.italic = True
    r2.font.size = Pt(9)
    doc.add_paragraph() # space

def main():
    doc = docx.Document('SI886-PLANTILLA-TALLER.docx')

    # 1. Carátula
    for p in doc.paragraphs[:28]:
        t = p.text.strip()
        if "……………………………………………." in t or ("TALLER" in t and "“" in t):
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
        elif "DR. OSCAR JUAN JIMENEZ FLORES" in t or "DR." in t:
            p.text = "DR. OSCAR JUAN JIMENEZ FLORES"
            p.style = doc.styles['Centrado']
            for run in p.runs:
                run.font.bold = True
                run.font.size = Pt(11)
        elif "TACNA — PERÚ" in t:
            p.text = "TACNA — PERÚ\n2026"
            p.style = doc.styles['Centrado']
            for run in p.runs:
                run.font.bold = True

    # 2. Localizar y remover los párrafos de instrucciones y el cuerpo previo
    # Localizar dónde termina el TOC y dónde empieza el contenido
    # Buscamos '7. Anexos\t1' o similar en TOC
    idx_fin_toc = -1
    for i, p in enumerate(doc.paragraphs):
        if "7. Anexos" in p.text and "\t" in p.text:
            idx_fin_toc = i
            break

    # Remover desde idx_fin_toc + 1 hasta el final
    # También remover todas las tablas existentes en la plantilla para reconstruirlas ordenadamente
    for tbl in list(doc.tables):
        tbl._element.getparent().remove(tbl._element)

    total_p = len(doc.paragraphs)
    for i in range(total_p - 1, idx_fin_toc, -1):
        p_elem = doc.paragraphs[i]._p
        p_elem.getparent().remove(p_elem)

    print(f"[OK] Carátula e Índice preservados. Procediendo a redactar secciones 1 a 7...")

    # Salto de página tras el índice
    doc.add_page_break()

    # =========================================================================
    # SECCIÓN 1: INFORMACIÓN SOBRE EL EVENTO PRÁCTICO
    # =========================================================================
    h1 = doc.add_heading('1. Información sobre el evento práctico', level=1)
    
    doc.add_heading('1.1 Título del evento práctico', level=2)
    p = doc.add_paragraph('Construcción del Portafolio de Proyectos de TI (Sección 7.1 del Plan Estratégico de Tecnologías de Información - PETI 2026–2030) para la Empresa Prestadora de Servicios de Saneamiento EPS AGUAS DEL SUR S.A.')
    
    doc.add_heading('1.2 Objetivos', level=2)
    objs = [
        "Consolidar los candidatos a proyectos de TI provenientes de las cinco fuentes admisibles de arquitectura y gobernanza institucional.",
        "Depurar el portafolio mediante un estricto control de admisión, fusionando iniciativas con alcance duplicado y descartando candidatos no trazables a objetivos estratégicos.",
        "Elaborar la ficha técnica estandarizada de 20 campos para cada uno de los proyectos aprobados en el portafolio.",
        "Calcular el Costo Total de Propiedad (TCO a cinco años) de cada proyecto, determinando el Capex inicial con su margen de incertidumbre, el Opex recurrente anual y el factor TCO/Inversión.",
        "Desarrollar el caso de negocio integral para los tres proyectos de mayor inversión de capital, evaluando tres alternativas por iniciativa y cuantificando rigurosamente el costo de la inacción (Alternativa 0).",
        "Evaluar cuantitativa y cualitativamente el impacto de cada proyecto en el desarrollo sostenible sobre las cinco dimensiones normadas: Sociedad, Economía, Salud y Seguridad, Marco Legal y Medio Ambiente.",
        "Analizar el balance estratégico del portafolio en las categorías Operar (Run), Crecer (Grow) y Transformar (Transform), contrastándolo críticamente con la línea base del presupuesto actual de TI de la empresa.",
        "Construir el mapa de dependencias técnicas entre proyectos mediante teoría de grafos y obtener el orden topológico de ejecución que condiciona la hoja de ruta institucional (Sección 7.3).",
        "Redactar formalmente la Sección 7.1 del PETI en formato Markdown estructurado y registrar las evidencias completas en el repositorio GitHub bajo las etiquetas de versión correspondientes."
    ]
    for o in objs:
        p_obj = doc.add_paragraph(f"• {o}", style='Compact' if 'Compact' in [s.name for s in doc.styles] else 'Normal')
        p_obj.paragraph_format.left_indent = Inches(0.25)

    doc.add_heading('1.3 Tiempo de duración', level=2)
    doc.add_paragraph('Duración programada: 4 horas de sesión de laboratorio de cómputo presencial más 6 horas de trabajo de investigación y desarrollo grupal no presencial.')

    doc.add_heading('1.4 Resultados de aprendizaje', level=2)
    doc.add_paragraph(
        'El equipo de trabajo demuestra dominio procedimental en la formulación, tamizaje, priorización y costeo plurianual de iniciativas tecnológicas para organizaciones de servicios públicos. '
        'Aplica con solvencia técnica las directivas de gobierno digital (R.S.G.D. 005-2018-PCM/SEGDI), los lineamientos de gobierno de TI de COBIT 2019 (objetivos APO05 y EDM02), el estándar Val IT y los principios de gestión de proyectos de PMBOK e ISO 21500, '
        'sustentando decisiones de inversión mediante indicadores financieros (TCO, VAN, Capex/Opex) y métricas de valor público.'
    )

    doc.add_heading('1.5 Recursos', level=2)
    doc.add_paragraph('A continuación se detallan las tecnologías, herramientas informáticas y fuentes de datos empleadas en el desarrollo del taller:')

    t_rec = doc.add_table(rows=1, cols=3)
    t_rec.rows[0].cells[0].text = "Recurso / Tecnología"
    t_rec.rows[0].cells[1].text = "Versión / Tipo"
    t_rec.rows[0].cells[2].text = "Para qué se usó en el taller"
    
    recursos_data = [
        ("Python", "3.13.15 (64-bit)", "Ejecución de scripts de análisis, consolidación de candidatos, cálculo de TCO, grafo de dependencias y balance."),
        ("pandas", "3.1.1", "Procesamiento matricial de datos de candidatos, cálculo financiero plurianual de TCO y análisis de presupuesto."),
        ("networkx", "3.7", "Construcción y validación del Grafo Acíclico Dirigido (DAG), cálculo de grados de salida y orden topológico."),
        ("matplotlib", "3.11.2", "Generación automatizada de infografías y gráficos de alta resolución (PF_balance.png, PF_tco.png, PF_dependencias.png)."),
        ("Git / GitHub", "2.47+ / Cloud", "Control de versiones distribuido del repositorio del PETI, trazabilidad de código y etiquetado formal (v0.13 y taller-13)."),
        ("python-docx", "1.2.0", "Automatización de la redacción técnica estructurada y estilización del informe en formato Microsoft Word."),
        ("Microsoft Word / Office", "2016 / 365 ProPlus", "Renderizado final de tipografías, actualización de campos de tabla de contenido y exportación conforme a PDF."),
        ("Datos: presupuesto_ti.csv", "Línea Base EPS", "Análisis de la estructura de gasto actual de TI de EPS AGUAS DEL SUR S.A. (S/ 1,080,000 anuales)."),
        ("Datos: expedientes-de-inversion.md", "Línea Base EPS", "Diagnóstico de desviaciones históricas (+62.5%, +34.0%, +32.9%) y lecciones aprendidas en proyectos cerrados."),
        ("Datos: pagos.csv", "Transaccional EPS", "Validación de costos reales de mercado en proveedores informáticos para estimación del Opex plurianual.")
    ]
    for r1, r2, r3 in recursos_data:
        row = t_rec.add_row()
        row.cells[0].text = r1
        row.cells[1].text = r2
        row.cells[2].text = r3
    style_table(t_rec, [2.0, 1.5, 3.5])

    doc.add_heading('1.6 Seguridad', level=2)
    sec_points = [
        "Confidencialidad de la Información: Los expedientes de inversión, presupuestos y registros de pagos de EPS AGUAS DEL SUR S.A. son tratados con reserva institucional y estrictamente para fines académicos.",
        "Rango de Incertidumbre en Estimaciones: En concordancia con las buenas prácticas de ingeniería de costos, ninguna estimación de inversión se presentó como cifra cerrada; se declararon rangos explícitos de incertidumbre (±15% a ±20%) sustentados en datos históricos de compras reales (pagos.csv).",
        "Ética Comercial: No se generaron solicitudes de cotización formales ni compromisos contractuales ficticios ante proveedores de tecnología en nombre de la organización sin la debida autorización.",
        "Seguridad de Entorno: Todo el software de análisis se ejecutó en ambientes aislados y seguros, garantizando la inmutabilidad de los datos fuente."
    ]
    for sp in sec_points:
        p_sec = doc.add_paragraph(f"• {sp}", style='Compact' if 'Compact' in [s.name for s in doc.styles] else 'Normal')
        p_sec.paragraph_format.left_indent = Inches(0.25)

    # =========================================================================
    # SECCIÓN 2: PROCEDIMIENTO O METODOLOGÍA
    # =========================================================================
    doc.add_page_break()
    doc.add_heading('2. Procedimiento o metodología', level=1)
    doc.add_paragraph(
        'El procedimiento metodológico aplicado por el equipo sigue el marco secuencial riguroso establecido para la construcción del portafolio del PETI. '
        'Abarca desde el tamizaje de iniciativas preliminares hasta el versionamiento final en GitHub, pasando por el modelado financiero de TCO a 5 años, '
        'el diseño de casos de negocio con cuantificación del costo de la inacción y el ordenamiento topológico por dependencias.'
    )

    # Paso A
    doc.add_heading('Paso A — Consolidar y depurar los candidatos a proyecto', level=2)
    doc.add_paragraph(
        'Las iniciativas no se crearon de manera aislada ni empírica. Se consolidaron candidatos provenientes de las cinco fuentes admisibles del PETI: '
        '1) Diagnóstico y Madurez de TI (Sección 3.5), 2) Arquitectura de Información y Datos (Sección 4.1.5), 3) Arquitectura de Aplicaciones (Sección 4.3.5), '
        '4) Arquitectura Tecnológica e Infraestructura (Sección 5.4.2), y 5) Necesidades Estratégicas y Gobierno Digital (Sección 6.1.7).'
    )
    doc.add_paragraph(
        'Se programó y ejecutó el script 07_portafolio/PF01_consolidacion.py para automatizar el control de admisión sobre 15 iniciativas preliminares (C-01 a C-15):'
    )
    p_code = doc.add_paragraph(
        '# Ejecución del Control de Admisión\n'
        'python 07_portafolio/PF01_consolidacion.py', style='Source Code' if 'Source Code' in [s.name for s in doc.styles] else 'Normal'
    )
    doc.add_paragraph(
        'Criterios de depuración aplicados:\n'
        '• Fusión de Alcance: La iniciativa C-03 (Telemetría en reservorios) fue FUSIONADA formalmente dentro de C-02 para conformar el proyecto PR-02 (Plataforma SCADA e Infraestructura IoT de Telemetría), '
        'evitando compras fragmentadas y asegurando una plataforma de control unificada.\n'
        '• Retiro de Candidatos Inadmisibles: Las iniciativas C-14 (Renovación de impresoras) y C-15 (Software de diseño 3D para relaciones públicas) fueron RETIRADAS por no provenir de ninguna de las fuentes '
        'admisibles de arquitectura, no resolver brechas estructurales y carecer de alineamiento con los objetivos estratégicos institucionales (corresponden a gasto corriente administrativo).'
    )
    doc.add_paragraph('El proceso depuró el portafolio en exactamente 12 proyectos estratégicos oficiales, exportados a 07_portafolio/PF01_portafolio_candidatos.csv.')

    # Paso B
    doc.add_heading('Paso B — Ficha estandarizada y Costo Total de Propiedad (TCO)', level=2)
    doc.add_paragraph(
        'Para garantizar la gobernanza del portafolio (COBIT APO05.03), cada proyecto cuenta con su Ficha Técnica Estandarizada de 20 campos archivada en formato Markdown versionable en 07_portafolio/PF03_fichas/ (desde PR-01.md hasta PR-12.md). '
        'Los 20 campos cubren: Código, Nombre, Fuente, Sección origen, Objetivo estratégico, Categoría, Justificación, Alcance, Entregables, Sponsor, Beneficiarios, Plazo, Capex con incertidumbre, Opex anual, TCO a 5 años, Beneficios, Riesgos y mitigación, Dependencias, Sostenibilidad y KPIs.'
    )
    doc.add_paragraph(
        'Cálculo del Costo Total de Propiedad (TCO a 5 Años): Se programó el script 07_portafolio/PF02_tco.py, integrando la inversión de capital inicial (Capex) con el gasto operativo plurianual recurrente (Opex anual × 5), '
        'sustentado en la estructura de pagos históricos a proveedores de TI (pagos.csv):'
    )

    # Tabla resumen de TCO en el DOCX
    t_tco = doc.add_table(rows=1, cols=6)
    t_tco.rows[0].cells[0].text = "ID"
    t_tco.rows[0].cells[1].text = "Proyecto Estratégico"
    t_tco.rows[0].cells[2].text = "Inversión (Capex)"
    t_tco.rows[0].cells[3].text = "Opex Anual"
    t_tco.rows[0].cells[4].text = "TCO 5 Años (S/)"
    t_tco.rows[0].cells[5].text = "Factor"

    tco_rows = [
        ("PR-01", "SIGECO-Agua (Comercial y Facturación)", "S/ 380,000.00", "S/ 65,000.00", "S/ 705,000.00", "1.86x"),
        ("PR-02", "SCADA e Infraestructura IoT Telemetría", "S/ 420,000.00", "S/ 72,000.00", "S/ 780,000.00", "1.86x"),
        ("PR-03", "Nube Híbrida, Datacenter y DRP", "S/ 290,000.00", "S/ 75,000.00", "S/ 665,000.00", "2.29x"),
        ("PR-04", "Plataforma Omnicanal y Autoservicio", "S/ 160,000.00", "S/ 42,000.00", "S/ 370,000.00", "2.31x"),
        ("PR-05", "GIS Corporativo de Redes de Agua", "S/ 240,000.00", "S/ 48,000.00", "S/ 480,000.00", "2.00x"),
        ("PR-06", "Bus de Integración ESB / API Gateway", "S/ 150,000.00", "S/ 35,000.00", "S/ 325,000.00", "2.17x"),
        ("PR-07", "Repositorio Maestro MDM y BI", "S/ 180,000.00", "S/ 38,000.00", "S/ 370,000.00", "2.06x"),
        ("PR-08", "CMMS / GMAO Mantenimiento Activos", "S/ 140,000.00", "S/ 32,000.00", "S/ 300,000.00", "2.14x"),
        ("PR-09", "Ciberseguridad Redes OT/IT y SOC", "S/ 190,000.00", "S/ 55,000.00", "S/ 465,000.00", "2.45x"),
        ("PR-10", "Monitoreo Calidad de Agua en Línea", "S/ 210,000.00", "S/ 45,000.00", "S/ 435,000.00", "2.07x"),
        ("PR-11", "Red WAN Enlaces Redundantes Remotos", "S/ 130,000.00", "S/ 52,000.00", "S/ 390,000.00", "3.00x"),
        ("PR-12", "Respaldo Inmutable Anti-Ransomware", "S/ 120,000.00", "S/ 30,000.00", "S/ 270,000.00", "2.25x"),
        ("TOTAL", "PORTAFOLIO GLOBAL (12 PROYECTOS)", "S/ 2,610,000.00", "S/ 589,000.00", "S/ 5,555,000.00", "2.13x")
    ]
    for r in tco_rows:
        row = t_tco.add_row()
        for idx, val in enumerate(r):
            row.cells[idx].text = val
    style_table(t_tco, [0.8, 2.5, 1.1, 1.0, 1.1, 0.7])

    doc.add_paragraph()
    doc.add_paragraph(
        'Interpretación del Factor TCO / Inversión Inicial: El factor promedio del portafolio es de 2.13x. Esto indica que por cada sol invertido como Capex inicial, '
        'EPS AGUAS DEL SUR S.A. deberá destinar S/ 1.13 adicionales a lo largo de 5 años para su operación, soporte especializado y mantenimiento. '
        'Los proyectos con mayor carga operativa recurrente son PR-11 (Red WAN, factor 3.00x) y PR-09 (Ciberseguridad SOC, factor 2.45x), debido a que basan su valor en servicios mensuales continuos '
        '(enlaces satelitales Starlink y monitoreo SOC 24/7), superando con creces la inversión en equipamiento inicial.'
    )

    if os.path.exists("evidencias/S13/PF_tco.png"):
        doc.add_picture("evidencias/S13/PF_tco.png", width=Inches(6.2))
        p_cap = doc.add_paragraph("Figura 1: Costo Total de Propiedad (TCO a 5 Años) desagregado en Capex y Opex para los 12 proyectos del portafolio.", style='Caption' if 'Caption' in [s.name for s in doc.styles] else 'Normal')
        p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER

    # Paso C
    doc.add_heading('Paso C — Casos de negocio de los tres proyectos de mayor inversión', level=2)
    doc.add_paragraph(
        'Conforme a las directrices de PMBOK e ISO 21500, para los tres proyectos que demandan mayor inversión inicial se formuló el Caso de Negocio completo, '
        'evaluando cuantitativamente tres alternativas por proyecto mediante el script 07_portafolio/PF04_alternativas.py:'
    )
    doc.add_paragraph(
        '1. PR-02 (Plataforma SCADA e IoT de Telemetría — Capex S/ 420,000 | TCO S/ 780,000):\n'
        '   • Alternativa 0 (No hacer nada): Costo de inacción de -S/ 320,000 anuales (-S/ 1.60M a 5 años) por pérdidas continuas de agua potable (38% agua no facturada), consumo eléctrico excesivo en bombeo y multas SUNASS. VAN 5 años: -S/ 2,175,000.\n'
        '   • Alternativa 1 (Recomendada): SCADA modular abierto e IoT industrial (LoRaWAN/MQTT). VAN 5 años: S/ 1,270,000.\n'
        '   • Alternativa 2 (Propietario cerrado): Paquete monolítico de multinacional. Capex S/ 680K, VAN S/ 645K (descartada por sobrecosto del 67% y vendor lock-in).'
    )
    doc.add_paragraph(
        '2. PR-01 (SIGECO-Agua Gestión Comercial y Facturación — Capex S/ 380,000 | TCO S/ 705,000):\n'
        '   • Alternativa 0 (No hacer nada): Costo de inacción de -S/ 290,000 anuales (-S/ 1.45M a 5 años) por recibos erróneos, retrasos de 12 días en facturación y riesgo tributario SUNAT. VAN 5 años: -S/ 1,940,000.\n'
        '   • Alternativa 1 (Recomendada): Solución comercial cloud-native especializada en saneamiento con app móvil de toma de lecturas con GPS y facturación electrónica. VAN 5 años: S/ 1,220,000.\n'
        '   • Alternativa 2 (Desarrollo in-house desde cero): Capex S/ 490K, plazo incierto (>24 meses), VAN S/ 660K (descartada por alto riesgo de desvío presupuestal como ocurrió en el Expediente 1).'
    )
    doc.add_paragraph(
        '3. PR-03 (Nube Híbrida, Datacenter de Contingencia y DRP — Capex S/ 290,000 | TCO S/ 665,000):\n'
        '   • Alternativa 0 (No hacer nada): Costo de inacción valor esperado de -S/ 240,000 anuales (-S/ 1.20M a 5 años) por riesgo inminente de paralización total sin recuperación ante sismos de gran magnitud o ransomware. VAN 5 años: -S/ 1,625,000.\n'
        '   • Alternativa 1 (Recomendada): Infraestructura hiperconvergente local con replicación activa-pasiva hacia nube pública Tier III (AWS/Azure) con RPO < 15 min y RTO < 2 horas. VAN 5 años: S/ 735,000.\n'
        '   • Alternativa 2 (Segundo Datacenter físico en Planta Calana): Capex S/ 580K, TCO S/ 1.13M, VAN S/ 220K (descartada por costo civil desproporcionado en zona sísmica).'
    )

    add_callout(doc, 'La cuantificación explícita de la Alternativa 0 («No hacer nada») con beneficio negativo demuestra con cifras irrefutables ante el Directorio que la inacción no es gratuita: continuar como hoy le cuesta a la EPS más de S/ 850,000 al año en pérdidas operacionales y comerciales.', 'HALLAZGO CRÍTICO')

    # Paso D
    doc.add_heading('Paso D — Balance del portafolio y mapa de dependencias', level=2)
    doc.add_paragraph(
        'Análisis del Balance Operar / Crecer / Transformar (PF05_balance.py): Se contrastó la distribución de recursos del nuevo portafolio frente al presupuesto histórico de la empresa (presupuesto_ti.csv). '
        'El diagnóstico reveló que actualmente EPS AGUAS DEL SUR S.A. destina el 92.0% de su presupuesto a Operar (gasto corriente en licencias, soporte correctivo y personal) y apenas un 8.0% a Proyectos Nuevos (Inversión). '
        'El nuevo portafolio PETI rompe este esquema vicioso asignando el 39.8% de la inversión a Transformar y 37.9% a Crecer, reduciendo la inversión en Operar a 22.2% para modernizar estructuralmente la empresa.'
    )

    if os.path.exists("evidencias/S13/PF_balance.png"):
        doc.add_picture("evidencias/S13/PF_balance.png", width=Inches(6.2))
        p_cap2 = doc.add_paragraph("Figura 2: Balance de Inversión Inicial (Capex) del Portafolio y contraste con el Presupuesto Actual de TI y estándares de industria.", style='Caption' if 'Caption' in [s.name for s in doc.styles] else 'Normal')
        p_cap2.alignment = WD_ALIGN_PARAGRAPH.CENTER

    doc.add_paragraph(
        'Mapa de Dependencias y Orden Topológico (PF06_dependencias.py): Mediante la librería networkx se modelaron las 16 relaciones de dependencia técnica entre los 12 proyectos, '
        'comprobándose que la red conforma un Grafo Acíclico Dirigido (DAG) perfecto sin ciclos. '
        'Se identificaron los proyectos habilitadores clave (aquellos con mayor número de proyectos dependientes que deben ejecutarse prioritariamente con independencia de su retorno financiero directo):'
    )
    doc.add_paragraph(
        '• PR-06 (Bus de Integración ESB / API Gateway): Habilita a 4 proyectos (PR-01, PR-04, PR-05, PR-10).\n'
        '• PR-02 (SCADA e IoT de Telemetría): Habilita a 3 proyectos (PR-05, PR-08, PR-10).\n'
        '• PR-11 (Red WAN Enlaces Redundantes Remotos): Habilita a 2 proyectos (PR-02, PR-09).\n'
        '• PR-12 (Respaldo Inmutable Anti-Ransomware): Habilita a 2 proyectos (PR-03, PR-09).\n'
        '• PR-07 (Repositorio Maestro MDM y BI): Habilita a 2 proyectos (PR-01, PR-05).\n'
        '• PR-03 (Nube Híbrida y DRP): Habilita a 2 proyectos (PR-01, PR-04).'
    )
    doc.add_paragraph(
        'El algoritmo determinó la secuencia óptima en orden topológico: '
        'Paso 01: PR-06 → Paso 02: PR-07 → Paso 03: PR-11 → Paso 04: PR-12 → Paso 05: PR-02 → Paso 06: PR-03 → Paso 07: PR-09 → Paso 08: PR-05 → Paso 09: PR-08 → Paso 10: PR-10 → Paso 11: PR-01 → Paso 12: PR-04. '
        'Esta secuencia técnica rige de manera obligatoria la Hoja de Ruta de Implementación (Sección 7.3).'
    )

    if os.path.exists("evidencias/S13/PF_dependencias.png"):
        doc.add_picture("evidencias/S13/PF_dependencias.png", width=Inches(6.2))
        p_cap3 = doc.add_paragraph("Figura 3: Mapa de dependencias técnicas y capas arquitectónicas entre los proyectos del portafolio.", style='Caption' if 'Caption' in [s.name for s in doc.styles] else 'Normal')
        p_cap3.alignment = WD_ALIGN_PARAGRAPH.CENTER

    # Paso E
    doc.add_heading('Paso E — Redactar Sección 7.1 del PETI', level=2)
    doc.add_paragraph(
        'Se elaboró el documento formal Markdown 07_portafolio/7.1_portafolio_de_proyectos.md conteniendo las ocho subsecciones exigidas:\n'
        '7.1.1 Fuentes admisibles y control de admisión; 7.1.2 Portafolio de proyectos; 7.1.3 Fichas de proyecto; 7.1.4 Costo total de propiedad; '
        '7.1.5 Casos de negocio de los tres mayores; 7.1.6 Balance del portafolio; 7.1.7 Dependencias entre proyectos; y 7.1.8 Cobertura de objetivos estratégicos.'
    )

    # Paso F
    doc.add_heading('Paso F — Validar y corregir', level=2)
    doc.add_paragraph(
        'Se implementó y ejecutó el script 07_portafolio/verificar_cobertura.py, comprobando tres reglas de calidad metodológica:\n'
        '1. Cada proyecto cita con precisión el objetivo estratégico de la sección 6.2 al que responde: VERIFICADO (100% de proyectos alineados a OE-01, OE-02, OE-03, OE-04 o OE-05).\n'
        '2. Los duplicados fusionados no perdieron alcance: VERIFICADO (C-03 quedó completamente integrada con sus sensores y telemetría en PR-02).\n'
        '3. El TCO a 5 años incluye rigurosamente el gasto operativo recurrente: VERIFICADO (100% de proyectos con Opex plurianual mayor a cero, alcanzando S/ 589K/año en régimen).'
    )

    # Paso G
    doc.add_heading('Paso G — Registrar la evidencia y cerrar', level=2)
    doc.add_paragraph(
        'Se ejecutó el versionamiento formal en Git, registrando el commit descriptivo y generando las etiquetas exigidas:\n'
        '• git commit -m "S13: portafolio de proyectos, TCO, casos de negocio y dependencias -- seccion 7.1"\n'
        '• git tag -a v0.13 -m "PETI v0.13 -- portafolio de proyectos"\n'
        '• git tag -a taller-13 -m "Taller 13 · SI886"\n'
        'Todas las evidencias, programas, salidas de consola (.txt) y gráficos (.png) quedaron asegurados para la subida manual al repositorio remoto.'
    )

    # =========================================================================
    # SECCIÓN 3: RESULTADOS
    # =========================================================================
    doc.add_page_break()
    doc.add_heading('3. Resultados', level=1)
    doc.add_paragraph(
        'A continuación se presenta la Lista de Comprobación 3.2 de la guía de taller, evaluando el cumplimiento de cada resultado esperado y '
        'consignando la URL de verificación en el repositorio GitHub bajo la etiqueta oficial taller-13:'
    )

    # Tabla de Resultados (13 filas)
    t_res = doc.add_table(rows=1, cols=4)
    t_res.rows[0].cells[0].text = "#"
    t_res.rows[0].cells[1].text = "Resultado Esperado"
    t_res.rows[0].cells[2].text = "¿Se logró?"
    t_res.rows[0].cells[3].text = "Evidencia / Enlace en Repositorio GitHub (tag: taller-13)"

    repo_base = "https://github.com/mauchoquenachoque/PETI-SEMANA13-CHOQUENA-CALLOTICONA-RAMOSL/tree/taller-13"

    resultados_data = [
        ("1", "Candidatos consolidados desde las cinco fuentes admisibles", "LOGRADO", f"{repo_base}/07_portafolio/PF01_portafolio_candidatos.csv"),
        ("2", "Control de admisión ejecutado. Candidatos sin fuente o sin objetivo retirados", "LOGRADO", f"{repo_base}/evidencias/S13/salidas/salida_PF01.txt"),
        ("3", "Portafolio con ≥ 12 proyectos, cada uno con su sección de origen citada", "LOGRADO", f"{repo_base}/07_portafolio/PF01_portafolio_candidatos.csv"),
        ("4", "Ficha estandarizada de cada proyecto con los 20 campos completos", "LOGRADO", f"{repo_base}/07_portafolio/PF03_fichas/"),
        ("5", "TCO a 5 años calculado para cada proyecto, con margen de incertidumbre", "LOGRADO", f"{repo_base}/07_portafolio/PF02_tco.csv"),
        ("6", "Factor TCO/inversión inicial calculado e interpretado (global 2.13x)", "LOGRADO", f"{repo_base}/evidencias/S13/salidas/salida_PF02.txt"),
        ("7", "Tres casos de negocio con las tres alternativas, incluida «no hacer nada»", "LOGRADO", f"{repo_base}/07_portafolio/PF04_alternativas.csv"),
        ("8", "Costo de la inacción cuantificado en cada caso de negocio con beneficio negativo", "LOGRADO", f"{repo_base}/evidencias/S13/salidas/salida_PF04.txt"),
        ("9", "Balance operar/crecer/transformar calculado y contrastado con presupuesto actual", "LOGRADO", f"{repo_base}/evidencias/S13/salidas/salida_PF05.txt"),
        ("10", "Gráficos de balance y de TCO por proyecto en alta resolución", "LOGRADO", f"{repo_base}/evidencias/S13/PF_balance.png"),
        ("11", "Mapa de dependencias con orden topológico y proyectos habilitadores", "LOGRADO", f"{repo_base}/evidencias/S13/PF_dependencias.png"),
        ("12", "Cobertura verificada: todo objetivo de la sección 6.2 con al menos un proyecto", "LOGRADO", f"{repo_base}/evidencias/S13/salidas/salida_cobertura.txt"),
        ("13", "Sección 7.1 redactada en Markdown · etiquetas v0.13 y taller-13", "LOGRADO", f"{repo_base}/07_portafolio/7.1_portafolio_de_proyectos.md")
    ]

    for num, re, log, url in resultados_data:
        row = t_res.add_row()
        row.cells[0].text = num
        row.cells[1].text = re
        row.cells[2].text = log
        row.cells[3].text = url
    style_table(t_res, [0.4, 2.5, 0.9, 3.4])

    doc.add_paragraph()
    doc.add_paragraph(
        'Sustentación de Resultados Logrados: Todos los 13 resultados requeridos por la lista de comprobación procedimental han sido alcanzados al 100%. '
        'El portafolio depurado contiene exactamente 12 proyectos vinculados a los cinco objetivos estratégicos de la EPS (OE-01 a OE-05), '
        'respaldados por sus 12 fichas individuales de 20 campos, cálculos financieros de TCO a 5 años, análisis del costo de inacción para los 3 mayores, '
        'contraste de balance frente al presupuesto histórico (presupuesto_ti.csv) y grafo de red con orden topológico verificado.'
    )

    # =========================================================================
    # SECCIÓN 4: CONCLUSIONES
    # =========================================================================
    doc.add_page_break()
    doc.add_heading('4. Conclusiones', level=1)
    
    conclusiones = [
        ("1. El TCO plurianual evita compromisos presupuestales ciegos ante la alta dirección:",
         "El cálculo del Costo Total de Propiedad a cinco años demostró un factor promedio de 2.13x (Capex de S/ 2.61M vs TCO de S/ 5.55M). "
         "Presentar exclusivamente la inversión inicial ante el Directorio hubiese comprometido a EPS AGUAS DEL SUR S.A. con un gasto operativo recurrente de S/ 2.94M que nunca fue aprobado formalmente. "
         "En servicios públicos, donde las tarifas y presupuestos son regulados por SUNASS, el conocimiento transparente del Opex anual (S/ 589K en régimen) es vital para asegurar la sostenibilidad del servicio."),
        
        ("2. El costo cuantificado de la inacción es el argumento más contundente del caso de negocio:",
         "La formulación de la Alternativa 0 («No hacer nada») con beneficio negativo en los tres proyectos mayores (PR-02: -S/ 320K/año, PR-01: -S/ 290K/año, PR-03: -S/ 240K/año) "
         "demostró que mantener el status quo le genera a la empresa pérdidas acumuladas superiores a S/ 4.25M en cinco años por agua no facturada, fallas de facturación y paradas de servicio. "
         "Esta cifra desmantela la falsa premisa de que postergar inversiones de TI no tiene costo."),
         
        ("3. Los proyectos habilitadores poseen prioridad estructural independientemente de su retorno directo:",
         "Proyectos como el Bus de Integración de Servicios (PR-06), el Repositorio Maestro de Datos (PR-07) y la Red WAN Redundante (PR-11) no producen facturación ni retorno financiero directo, "
         "pero sin ellos es técnicamente inviable operar la plataforma comercial (PR-01), el autoservicio web/móvil (PR-04), el GIS (PR-05) o la telemetría SCADA (PR-02). "
         "Priorizar iniciativas únicamente por su VAN individual condena al fracaso el portafolio institucional."),
         
        ("4. Reorientación estratégica: Romper la trampa del gasto operativo reactivo:",
         "El contraste con la línea base presupuestal reveló que EPS AGUAS DEL SUR S.A. destina actualmente el 92.0% de sus recursos a sostener la operación cotidiana (Run), dejando un insignificante 8.0% a inversión nueva. "
         "El portafolio PETI rompe esta trampa reactiva al orientar el 77.7% del Capex hacia Transformar (39.8%) y Crecer (37.9%), canalizando recursos hacia la automatización con telemetría IoT, "
         "recaudación electrónica y gestión georreferenciada de pérdidas hídricas.")
    ]
    for c_tit, c_desc in conclusiones:
        p_c = doc.add_paragraph()
        r_ct = p_c.add_run(c_tit + " ")
        r_ct.font.bold = True
        r_ct.font.size = Pt(10)
        r_cd = p_c.add_run(c_desc)
        r_cd.font.size = Pt(9.5)

    # =========================================================================
    # SECCIÓN 5: CUESTIONARIO
    # =========================================================================
    doc.add_page_break()
    doc.add_heading('5. Cuestionario', level=1)
    
    doc.add_heading('Pregunta de transferencia: ¿Qué riesgo correría una organización real si este proceso se hiciera mal o se omitiera?', level=2)
    doc.add_paragraph(
        'Si una organización real —particularmente una empresa pública de saneamiento como EPS AGUAS DEL SUR S.A.— construye su portafolio de TI de forma improvisada, '
        'sin control de admisión, sin estimación de TCO plurianual y sin dependencias técnicas, se expone a cuatro categorías de riesgos catastróficos comprobados en los expedientes de inversión cerrados:'
    )

    riesgos_detallados = [
        ("A. Riesgo Financiero y Sobrecostos Descontrolados (Lección Expedientes 1, 2 y 3):",
         "Aprobar proyectos evaluando únicamente la orden de compra inicial sin prever el Opex conduce a desviaciones presupuestales masivas. "
         "Tal como ocurrió en el Expediente 1 (Portal de autoservicio con +62.5% de desviación presupuestal) y en el Expediente 2 (Sistema de respaldo con +34.0%), "
         "la empresa se ve obligada a desviar fondos operativos o paralizar proyectos a medio camino por falta de presupuesto para pagar soporte, hosting o enlaces de datos."),
        
        ("B. Riesgo de Arquitectura y Bloqueo Operacional por Falta de Habilitadores:",
         "Comprar aplicaciones de negocio (como el GIS o el sistema comercial) antes de contar con la capa de integración (ESB) o la red de comunicaciones adecuada "
         "produce islas tecnológicas ('silos') que no dialogan entre sí. Los operadores deben transferir datos manualmente en hojas de cálculo, "
         "aumentando los errores de digitación en un 300% y anulando los beneficios prometidos."),
        
        ("C. Riesgo Regulatorio y Sanciones Económicas de SUNASS y DIGESA:",
         "Las empresas prestadoras de saneamiento están sujetas a metas de gestión obligatorias (nivel de micromedición, continuidad del servicio y calidad bacteriológica y química del agua potable). "
         "No priorizar la telemetría SCADA ni el monitoreo continuo de cloro residual expone a la empresa a multas que superan los cientos de miles de soles y a la intervención directa del organismo regulador."),
        
        ("D. Riesgo de Continuidad del Negocio y Secuestro de Información (Ransomware):",
         "Omitir la resiliencia en la nube (DRP) y el almacenamiento inmutable deja a la institución totalmente indefensa ante desastres sísmicos o ciberataques. "
         "La pérdida de la base de datos de usuarios y cobranzas detendría la facturación durante meses, provocando un colapso financiero irreparable.")
    ]
    for r_tit, r_desc in riesgos_detallados:
        p_r = doc.add_paragraph()
        rr_t = p_r.add_run(r_tit + " ")
        rr_t.font.bold = True
        rr_t.font.size = Pt(9.5)
        rr_d = p_r.add_run(r_desc)
        rr_d.font.size = Pt(9)

    doc.add_heading('Pregunta complementaria: ¿Cómo articulan COBIT 2019 (APO05 / EDM02) y Val IT la rendición de cuentas del portafolio?', level=2)
    doc.add_paragraph(
        'El marco COBIT 2019 articula la gestión del portafolio en dos niveles de gobierno:\n'
        '• Nivel de Dirección (EDM02 - Entrega Asegurada de Beneficios): Exige que el Directorio no apruebe proyectos como gastos aislados, '
        'sino que supervise continuamente que el valor pactado en el caso de negocio se materialice durante la operación real post-entrega. En el caso analizado, los expedientes históricos nunca midieron beneficios posteriores.\n'
        '• Nivel de Gestión (APO05 - Portafolio Gestionado): Establece la evaluación formal de alternativas, el balance entre inversiones de transformación y costos corrientes, '
        'y el retiro programado de sistemas legados obsoletos.\n'
        '• Val IT Framework: Complementa exigiendo que cada inversión cuente con un caso de negocio vivo y transparente, donde se reconozca el costo de la inacción y se asigne responsabilidad nominal a un sponsor del negocio.'
    )

    # =========================================================================
    # SECCIÓN 6: REFERENCIAS BIBLIOGRÁFICAS
    # =========================================================================
    doc.add_page_break()
    doc.add_heading('6. Referencias bibliográficas', level=1)
    
    refs = [
        "ISACA. (2018). COBIT 2019 Framework: Governance and Management Objectives (Objetivos APO05 Managed Portfolio y EDM02 Ensured Benefits Delivery). ISACA.",
        "ISACA. (2008). The Val IT Framework 2.0: Enterprise Value: Governance of IT Investments. Information Systems Audit and Control Association.",
        "ISO. (2021). ISO 21500:2021 Project, programme and portfolio management — Context and concepts. International Organization for Standardization.",
        "MINTIC Colombia. (2020). Guía para la construcción del Plan Estratégico de Tecnologías de la Información (PETI) — Marco de Arquitectura de TI y Catálogo de Proyectos. Ministerio de Tecnologías de la Información y las Comunicaciones.",
        "Project Management Institute. (2021). A Guide to the Project Management Body of Knowledge (PMBOK Guide) (7ma ed.). Project Management Institute.",
        "Project Management Institute. (2017). The Standard for Portfolio Management (4ta ed.). Project Management Institute.",
        "Resolución de Secretaría de Gobierno Digital N° 005-2018-PCM/SEGDI. (2018). Lineamientos para la formulación del Plan de Gobierno Digital (Anexo I: Portafolio de Proyectos del PGD). Diario Oficial El Peruano.",
        "Rodríguez Bermúdez, J. R. (2015). Planificación y dirección estratégica de tecnologías y sistemas de información. Editorial UOC. https://elibro.net/es/lc/bibliotecaupt/titulos/57875",
        "Superintendencia Nacional de Servicios de Saneamiento [SUNASS]. (2017). Reglamento General de Supervisión, Fiscalización y Sanción de las Empresas Prestadoras de Servicios de Saneamiento. R.C.D. N° 018-2017-SUNASS/CD."
    ]
    for rf in refs:
        p_rf = doc.add_paragraph(rf, style='Bibliography' if 'Bibliography' in [s.name for s in doc.styles] else 'Normal')
        p_rf.paragraph_format.left_indent = Inches(0.5)
        p_rf.paragraph_format.first_line_indent = Inches(-0.5)

    # =========================================================================
    # SECCIÓN 7: ANEXOS
    # =========================================================================
    doc.add_page_break()
    doc.add_heading('7. Anexos', level=1)
    
    doc.add_heading('Anexo A: Matriz Consolidada de Candidatos y Control de Admisión (PF01)', level=2)
    doc.add_paragraph('Tabla de las 15 iniciativas evaluadas en el control de admisión, detallando su fuente admisible, objetivo estratégico y estado de admisión:')

    t_anx_a = doc.add_table(rows=1, cols=6)
    t_anx_a.rows[0].cells[0].text = "ID"
    t_anx_a.rows[0].cells[1].text = "Iniciativa Candidata"
    t_anx_a.rows[0].cells[2].text = "Fuente / Sección"
    t_anx_a.rows[0].cells[3].text = "Obj."
    t_anx_a.rows[0].cells[4].text = "Cat."
    t_anx_a.rows[0].cells[5].text = "Estado / Decisión de Admisión"

    candidatos_anx = [
        ("C-01", "Sistema Comercial SIGECO-Agua", "Sec 4.3.5 Aplicaciones", "OE-02", "Transf.", "Aprobado (Proyecto PR-01)"),
        ("C-02", "Plataforma SCADA e IoT Redes", "Sec 5.4.2 Infraestructura", "OE-01", "Transf.", "Aprobado (Proyecto PR-02)"),
        ("C-03", "Telemetría IoT en Reservorios", "Sec 5.4.2 Infraestructura", "OE-01", "Transf.", "FUSIONADO en PR-02 (mismo alcance)"),
        ("C-04", "Nube Híbrida y DRP Contingencia", "Sec 5.4.2 Infraestructura", "OE-03", "Crecer", "Aprobado (Proyecto PR-03)"),
        ("C-05", "Omnicanalidad y Autoservicio", "Sec 6.1.7 Gob. Digital", "OE-05", "Crecer", "Aprobado (Proyecto PR-04)"),
        ("C-06", "GIS Corporativo de Redes", "Sec 4.1.5 Información", "OE-01", "Transf.", "Aprobado (Proyecto PR-05)"),
        ("C-07", "Bus Integración ESB / API Gateway", "Sec 4.3.5 Aplicaciones", "OE-04", "Crecer", "Aprobado (Proyecto PR-06)"),
        ("C-08", "MDM, Gobierno del Dato y BI", "Sec 4.1.5 Información", "OE-04", "Crecer", "Aprobado (Proyecto PR-07)"),
        ("C-09", "CMMS Mantenimiento de Activos", "Sec 3.5 Madurez TI", "OE-01", "Operar", "Aprobado (Proyecto PR-08)"),
        ("C-10", "Ciberseguridad Redes OT/IT y SOC", "Sec 5.4.2 Infraestructura", "OE-03", "Operar", "Aprobado (Proyecto PR-09)"),
        ("C-11", "Monitoreo Calidad de Agua", "Sec 6.1.7 Gob. Digital", "OE-01", "Crecer", "Aprobado (Proyecto PR-10)"),
        ("C-12", "Red WAN Enlaces Redundantes", "Sec 3.5 Madurez TI", "OE-03", "Operar", "Aprobado (Proyecto PR-11)"),
        ("C-13", "Respaldo Inmutable Anti-Ransomware", "Sec 3.5 Madurez TI", "OE-03", "Operar", "Aprobado (Proyecto PR-12)"),
        ("C-14", "Renovación Parque Impresoras", "No trazable (Gasto corriente)", "N/A", "Operar", "RETIRADO (No es proyecto PETI)"),
        ("C-15", "Licencias Software Diseño 3D", "No trazable (Gasto corriente)", "N/A", "Operar", "RETIRADO (No responde a objetivos)")
    ]
    for ca in candidatos_anx:
        row = t_anx_a.add_row()
        for idx, val in enumerate(ca):
            row.cells[idx].text = val
    style_table(t_anx_a, [0.6, 2.2, 1.4, 0.5, 0.7, 1.8])

    doc.add_page_break()
    doc.add_heading('Anexo B: Resumen de Fichas Técnicas de Proyecto (20 Campos)', level=2)
    doc.add_paragraph('Estructura normalizada de las fichas contenidas en la carpeta 07_portafolio/PF03_fichas/:')
    
    campos_desc = [
        "1. Código de Proyecto (PR-01 a PR-12) | 2. Nombre Oficial | 3. Fuente Admisible | 4. Sección Origen PETI",
        "5. Objetivo Estratégico (OE-01 a OE-05) | 6. Categoría Estratégica (Operar, Crecer, Transformar)",
        "7. Justificación y Caso de Necesidad | 8. Descripción y Alcance | 9. Entregables Principales",
        "10. Sponsor y Líder Técnico | 11. Área Usuaria y Beneficiarios | 12. Plazo de Ejecución (meses)",
        "13. Inversión Inicial (Capex) con Incertidumbre | 14. Opex Anual | 15. TCO a 5 Años y Factor",
        "16. Beneficios Cuantitativos y Cualitativos | 17. Riesgos y Plan de Mitigación | 18. Dependencias Técnicas",
        "19. Impacto en Desarrollo Sostenible (5 dimensiones) | 20. Indicador de Éxito / KPI Cuantificable"
    ]
    for c in campos_desc:
        doc.add_paragraph(f"• {c}")

    doc.add_heading('Anexo C: Matriz de Costo Total de Propiedad a 5 Años (PF02)', level=2)
    doc.add_paragraph('Detalle del TCO plurianual exportado en 07_portafolio/PF02_tco.csv, evidenciando el Capex inicial, el Opex anualizado y el factor multiplicador:')
    
    t_anx_c = doc.add_table(rows=1, cols=6)
    t_anx_c.rows[0].cells[0].text = "ID"
    t_anx_c.rows[0].cells[1].text = "Nombre"
    t_anx_c.rows[0].cells[2].text = "Capex"
    t_anx_c.rows[0].cells[3].text = "Opex/Año"
    t_anx_c.rows[0].cells[4].text = "Opex 5A"
    t_anx_c.rows[0].cells[5].text = "TCO 5A"
    
    tco_anx_data = [
        ("PR-01", "SIGECO-Agua Comercial", "S/ 380,000", "S/ 65,000", "S/ 325,000", "S/ 705,000"),
        ("PR-02", "SCADA e IoT Telemetría", "S/ 420,000", "S/ 72,000", "S/ 360,000", "S/ 780,000"),
        ("PR-03", "Nube Híbrida y DRP", "S/ 290,000", "S/ 75,000", "S/ 375,000", "S/ 665,000"),
        ("PR-04", "Omnicanalidad Autoservicio", "S/ 160,000", "S/ 42,000", "S/ 210,000", "S/ 370,000"),
        ("PR-05", "GIS Corporativo Redes", "S/ 240,000", "S/ 48,000", "S/ 240,000", "S/ 480,000"),
        ("PR-06", "Bus ESB / API Gateway", "S/ 150,000", "S/ 35,000", "S/ 175,000", "S/ 325,000"),
        ("PR-07", "MDM, Datos y BI", "S/ 180,000", "S/ 38,000", "S/ 190,000", "S/ 370,000"),
        ("PR-08", "CMMS Mantenimiento Activos", "S/ 140,000", "S/ 32,000", "S/ 160,000", "S/ 300,000"),
        ("PR-09", "Ciberseguridad y SOC", "S/ 190,000", "S/ 55,000", "S/ 275,000", "S/ 465,000"),
        ("PR-10", "Monitoreo Calidad Agua", "S/ 210,000", "S/ 45,000", "S/ 225,000", "S/ 435,000"),
        ("PR-11", "Red WAN Enlaces Remotos", "S/ 130,000", "S/ 52,000", "S/ 260,000", "S/ 390,000"),
        ("PR-12", "Respaldo Anti-Ransomware", "S/ 120,000", "S/ 30,000", "S/ 150,000", "S/ 270,000"),
        ("TOTAL", "12 PROYECTOS APROBADOS", "S/ 2,610,000", "S/ 589,000", "S/ 2,945,000", "S/ 5,555,000")
    ]
    for row_d in tco_anx_data:
        r = t_anx_c.add_row()
        for idx, val in enumerate(row_d):
            r.cells[idx].text = val
    style_table(t_anx_c, [0.8, 2.4, 1.0, 1.0, 1.0, 1.0])

    doc.add_page_break()
    doc.add_heading('Anexo D: Casos de Negocio, Alternativas y Costo de la Inacción (PF04)', level=2)
    doc.add_paragraph('Comparativa de las 9 alternativas analizadas para los 3 proyectos de mayor inversión en 07_portafolio/PF04_alternativas.csv:')

    t_anx_d = doc.add_table(rows=1, cols=6)
    t_anx_d.rows[0].cells[0].text = "Proyecto"
    t_anx_d.rows[0].cells[1].text = "Alternativa Evaluada"
    t_anx_d.rows[0].cells[2].text = "Capex"
    t_anx_d.rows[0].cells[3].text = "TCO 5A"
    t_anx_d.rows[0].cells[4].text = "VAN 5 Años"
    t_anx_d.rows[0].cells[5].text = "¿Recomendada?"

    alt_data = [
        ("PR-02", "Alt 0: No hacer nada (Status Quo)", "S/ 0", "S/ 575,000", "-S/ 2,175,000", "No"),
        ("PR-02", "Alt 1: SCADA Modular Abierto e IoT", "S/ 420,000", "S/ 780,000", "S/ 1,270,000", "SÍ"),
        ("PR-02", "Alt 2: SCADA Propietario Monomarca", "S/ 680,000", "S/ 1,305,000", "S/ 645,000", "No"),
        ("PR-01", "Alt 0: No hacer nada (Status Quo)", "S/ 0", "S/ 490,000", "-S/ 1,940,000", "No"),
        ("PR-01", "Alt 1: Cloud-Native Saneamiento", "S/ 380,000", "S/ 705,000", "S/ 1,220,000", "SÍ"),
        ("PR-01", "Alt 2: Desarrollo In-House a Medida", "S/ 490,000", "S/ 890,000", "S/ 660,000", "No"),
        ("PR-03", "Alt 0: No hacer nada (Status Quo)", "S/ 0", "S/ 425,000", "-S/ 1,625,000", "No"),
        ("PR-03", "Alt 1: Nube Híbrida Activa-Pasiva", "S/ 290,000", "S/ 665,000", "S/ 735,000", "SÍ"),
        ("PR-03", "Alt 2: Segundo Datacenter Físico", "S/ 580,000", "S/ 1,130,000", "S/ 220,000", "No")
    ]
    for ad in alt_data:
        r = t_anx_d.add_row()
        for idx, val in enumerate(ad):
            r.cells[idx].text = val
    style_table(t_anx_d, [0.8, 2.5, 0.9, 1.0, 1.2, 0.8])

    doc.add_heading('Anexo E: Gráficos de Balance del Portafolio y TCO (PF05 / PF02)', level=2)
    doc.add_paragraph('Imágenes generadas automáticamente durante el análisis:')
    if os.path.exists("evidencias/S13/PF_balance.png"):
        doc.add_picture("evidencias/S13/PF_balance.png", width=Inches(5.8))
    if os.path.exists("evidencias/S13/PF_tco.png"):
        doc.add_picture("evidencias/S13/PF_tco.png", width=Inches(5.8))

    doc.add_page_break()
    doc.add_heading('Anexo F: Mapa de Dependencias Técnicas y Orden Topológico (PF06)', level=2)
    doc.add_paragraph('Grafo de red acíclico y secuencia de ejecución generada con networkx:')
    if os.path.exists("evidencias/S13/PF_dependencias.png"):
        doc.add_picture("evidencias/S13/PF_dependencias.png", width=Inches(6.0))

    # Guardar documento final sobrescribiendo SI886-PLANTILLA-TALLER.docx
    doc_path = "SI886-PLANTILLA-TALLER.docx"
    doc.save(doc_path)
    print(f"[OK] Documento guardado exitosamente: {doc_path}")

if __name__ == "__main__":
    main()
