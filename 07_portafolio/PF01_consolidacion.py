"""
PF01_consolidacion.py
Consolidación de candidatos a proyectos de TI y Control de Admisión
EPS AGUAS DEL SUR S.A. - PETI 2026-2030 (Semana 13)
"""

import pandas as pd
import os

def consolidar_candidatos():
    candidatos_raw = [
        {
            "id_candidato": "C-01",
            "nombre": "Sistema Integrado de Gestión Comercial y Facturación Electrónica (SIGECO-Agua)",
            "fuente": "Arquitectura de Aplicaciones",
            "seccion_origen": "Sección 4.3.5",
            "objetivo_estrategico": "OE-02",
            "categoria": "Transformar",
            "descripcion": "Reemplazo del sistema comercial legado por una plataforma integral web/móvil con facturación electrónica SUNAT y recaudación descentralizada.",
            "estado": "Aprobado",
            "proyecto_id": "PR-01",
            "razon_decision": "Admitido: Cumple fuente admisible, alineado a OE-02 (recaudación y reducción de agua no facturada)."
        },
        {
            "id_candidato": "C-02",
            "nombre": "Plataforma SCADA e Infraestructura IoT de Telemetría de Redes Hidráulicas",
            "fuente": "Arquitectura Tecnológica e Infraestructura",
            "seccion_origen": "Sección 5.4.2",
            "objetivo_estrategico": "OE-01",
            "categoria": "Transformar",
            "descripcion": "Modernización de telemetría en reservorios y plantas de tratamiento con sensores IoT de caudal y presión en tiempo real.",
            "estado": "Aprobado",
            "proyecto_id": "PR-02",
            "razon_decision": "Admitido: Resuelve brecha crítica de continuidad operativa y macromedición."
        },
        {
            "id_candidato": "C-03",
            "nombre": "Telemetría IoT en Reservorios y Pozos Sectoriales",
            "fuente": "Arquitectura Tecnológica e Infraestructura",
            "seccion_origen": "Sección 5.4.2",
            "objetivo_estrategico": "OE-01",
            "categoria": "Transformar",
            "descripcion": "Sensores remotos de nivel de agua y caudalímetros en 8 reservorios principales.",
            "estado": "Fusionado",
            "proyecto_id": "PR-02",
            "razon_decision": "Fusionado en PR-02: Comparte alcance técnico e infraestructura de comunicaciones con la plataforma SCADA central."
        },
        {
            "id_candidato": "C-04",
            "nombre": "Nube Híbrida, Datacenter de Contingencia y Plan de Recuperación ante Desastres (DRP)",
            "fuente": "Arquitectura Tecnológica e Infraestructura",
            "seccion_origen": "Sección 5.4.2",
            "objetivo_estrategico": "OE-03",
            "categoria": "Crecer",
            "descripcion": "Implementación de arquitectura híbrida (nube + centro de datos local) con contingencia activa y failover ante sismos o fallas mayores.",
            "estado": "Aprobado",
            "proyecto_id": "PR-03",
            "razon_decision": "Admitido: Garantiza resiliencia institucional y continuidad de servicios críticos."
        },
        {
            "id_candidato": "C-05",
            "nombre": "Plataforma Omnicanal de Autoservicio y Atención al Usuario Ciudadano (Web/Móvil/WhatsApp)",
            "fuente": "Necesidades Estratégicas y Gobierno Digital",
            "seccion_origen": "Sección 6.1.7",
            "objetivo_estrategico": "OE-05",
            "categoria": "Crecer",
            "descripcion": "Reemplazo y superación del portal fallido del Expediente 1, integrando chatbot WhatsApp, pago en línea y seguimiento de reclamos SUNASS.",
            "estado": "Aprobado",
            "proyecto_id": "PR-04",
            "razon_decision": "Admitido: Cumple mandato de gobierno digital y soluciona la deuda técnica del portal 2024."
        },
        {
            "id_candidato": "C-06",
            "nombre": "Sistema de Información Geográfica (GIS) Corporativo para Redes de Agua y Alcantarillado",
            "fuente": "Arquitectura de Información y Datos",
            "seccion_origen": "Sección 4.1.5",
            "objetivo_estrategico": "OE-01",
            "categoria": "Transformar",
            "descripcion": "Catastro técnico georreferenciado de redes de distribución, tuberías, válvulas e hidrantes integrado con el catastro comercial.",
            "estado": "Aprobado",
            "proyecto_id": "PR-05",
            "razon_decision": "Admitido: Elimina islas de información física/cartográfica y reduce tiempos de reparación de fugas."
        },
        {
            "id_candidato": "C-07",
            "nombre": "Bus de Integración de Servicios (ESB / API Gateway) e Interoperabilidad",
            "fuente": "Arquitectura de Aplicaciones",
            "seccion_origen": "Sección 4.3.5",
            "objetivo_estrategico": "OE-04",
            "categoria": "Crecer",
            "descripcion": "Capa de servicios desacoplada para interconectar ERP, SIGECO, GIS, SCADA y la Plataforma Nacional de Interoperabilidad (PIDE/SUNASS).",
            "estado": "Aprobado",
            "proyecto_id": "PR-06",
            "razon_decision": "Admitido: Habilitador estructural crítico para el flujo transaccional y cumplimiento normativo."
        },
        {
            "id_candidato": "C-08",
            "nombre": "Repositorio Maestro de Datos (MDM), Gobierno del Dato y Plataforma de Analítica (BI)",
            "fuente": "Arquitectura de Información y Datos",
            "seccion_origen": "Sección 4.1.5",
            "objetivo_estrategico": "OE-04",
            "categoria": "Crecer",
            "descripcion": "Gobernanza del dato maestro de usuarios/suministros, pipeline ETL y dashboards gerenciales para control de pérdidas e ingresos.",
            "estado": "Aprobado",
            "proyecto_id": "PR-07",
            "razon_decision": "Admitido: Proyecto habilitador indispensable para analítica comercial y operacional confiable."
        },
        {
            "id_candidato": "C-09",
            "nombre": "Sistema de Gestión de Mantenimiento de Activos Electromecánicos y Redes (CMMS / GMAO)",
            "fuente": "Diagnóstico y Madurez de TI",
            "seccion_origen": "Sección 3.5",
            "objetivo_estrategico": "OE-01",
            "categoria": "Operar",
            "descripcion": "Software para gestión preventiva y correctiva de bombas, motores, válvulas y cuadrillas operativas en campo con órdenes de trabajo móviles.",
            "estado": "Aprobado",
            "proyecto_id": "PR-08",
            "razon_decision": "Admitido: Resuelve ineficiencias de mantenimiento manual reportadas en diagnóstico situacional."
        },
        {
            "id_candidato": "C-10",
            "nombre": "Fortalecimiento de la Ciberseguridad de Redes OT/IT y Centro de Operaciones de Seguridad (SOC)",
            "fuente": "Arquitectura Tecnológica e Infraestructura",
            "seccion_origen": "Sección 5.4.2",
            "objetivo_estrategico": "OE-03",
            "categoria": "Operar",
            "descripcion": "Segmentación de redes industriales SCADA (norma IEC 62443), SIEM, EDR en servidores y monitoreo 24/7 contra amenazas cibernéticas.",
            "estado": "Aprobado",
            "proyecto_id": "PR-09",
            "razon_decision": "Admitido: Protección de infraestructura crítica y mitigación de riesgos de sabotaje o secuestro de datos."
        },
        {
            "id_candidato": "C-11",
            "nombre": "Sistema de Monitoreo Automatizado de Calidad de Agua y Alerta Temprana",
            "fuente": "Necesidades Estratégicas y Gobierno Digital",
            "seccion_origen": "Sección 6.1.7",
            "objetivo_estrategico": "OE-01",
            "categoria": "Crecer",
            "descripcion": "Analizadores en línea de cloro residual, turbidez y pH en plantas y puntos testigo de red con telemetría de alerta inmediata a SUNASS.",
            "estado": "Aprobado",
            "proyecto_id": "PR-10",
            "razon_decision": "Admitido: Cumple normativa sanitaria D.S. 031-2010-SA y mandatos regulatorios de salud pública."
        },
        {
            "id_candidato": "C-12",
            "nombre": "Rediseño y Renovación de la Red WAN de Enlaces de Datos Redundantes para Estaciones Remotas",
            "fuente": "Diagnóstico y Madurez de TI",
            "seccion_origen": "Sección 3.5",
            "objetivo_estrategico": "OE-03",
            "categoria": "Operar",
            "descripcion": "Enlaces de fibra óptica y microondas licenciadas con respaldo satelital Starlink y SD-WAN para 14 plantas y reservorios periféricos.",
            "estado": "Aprobado",
            "proyecto_id": "PR-11",
            "razon_decision": "Admitido: Supera la falla de diseño y sobrecosto del Expediente 3, proveyendo redundancia real."
        },
        {
            "id_candidato": "C-13",
            "nombre": "Sistema Automatizado de Respaldo Corporativo Inmutable y Protección contra Ransomware",
            "fuente": "Diagnóstico y Madurez de TI",
            "seccion_origen": "Sección 3.5",
            "objetivo_estrategico": "OE-03",
            "categoria": "Operar",
            "descripcion": "Repositorio inmutable de respaldos (Air-gap / WORM) y automatización de pruebas de recuperación periódicas.",
            "estado": "Aprobado",
            "proyecto_id": "PR-12",
            "razon_decision": "Admitido: Corrige el fracaso del Expediente 2 asegurando capacidad de recuperación sin pago de rescates."
        },
        {
            "id_candidato": "C-14",
            "nombre": "Renovación de Parque de Impresoras y Escáneres de Oficinas Administrativas",
            "fuente": "Solicitud de Área Usuaria No Clasificada",
            "seccion_origen": "No trazable",
            "objetivo_estrategico": "No vinculado",
            "categoria": "Operar",
            "descripcion": "Compra directa de 45 equipos de impresión para diversas gerencias administrativas.",
            "estado": "Retirado",
            "proyecto_id": "N/A",
            "razon_decision": "Retirado en Control de Admisión: No proviene de ninguna de las cinco fuentes admisibles ni cuenta con justificación estratégica; corresponde a gasto corriente de abastecimiento."
        },
        {
            "id_candidato": "C-15",
            "nombre": "Adquisición de Licencias de Diseño Gráfico y Modelado 3D para Relaciones Públicas",
            "fuente": "Solicitud Departamental",
            "seccion_origen": "No trazable",
            "objetivo_estrategico": "No vinculado",
            "categoria": "Operar",
            "descripcion": "Licenciamiento anual de herramientas de diseño para imagen corporativa.",
            "estado": "Retirado",
            "proyecto_id": "N/A",
            "razon_decision": "Retirado en Control de Admisión: No responde a los objetivos estratégicos de TI ni a brechas de arquitectura institucional."
        }
    ]

    df_candidatos = pd.DataFrame(candidatos_raw)
    
    # Exportar CSV completo de control de admisión y candidatos
    csv_path = "07_portafolio/PF01_portafolio_candidatos.csv"
    df_candidatos.to_csv(csv_path, index=False, encoding="utf-8-sig")
    print(f"[OK] Archivo generado exitosamente: {csv_path}")
    print(f"Total de iniciativas evaluadas: {len(df_candidatos)}")
    
    # Estadísticas de admisión
    print("\n" + "="*70)
    print("CONTROL DE ADMISIÓN DE CANDIDATOS - EPS AGUAS DEL SUR S.A.")
    print("="*70)
    resumen_estados = df_candidatos['estado'].value_counts()
    for est, count in resumen_estados.items():
        print(f" - {est}: {count} candidatos")
    
    print("\nCANDIDATOS RETIRADOS O FUSIONADOS:")
    no_aprobados = df_candidatos[df_candidatos['estado'] != 'Aprobado']
    for _, r in no_aprobados.iterrows():
        print(f" * [{r['id_candidato']}] {r['nombre']} -> Estado: {r['estado']} | Razón: {r['razon_decision']}")

    print("\nPORTAFOLIO DE PROYECTOS APROBADOS (TOTAL: 12 PROYECTOS):")
    aprobados = df_candidatos[df_candidatos['estado'] == 'Aprobado'].sort_values('proyecto_id')
    for _, r in aprobados.iterrows():
        print(f" * [{r['proyecto_id']}] {r['nombre']} | Cat: {r['categoria']} | Fuente: {r['seccion_origen']} | Obj: {r['objetivo_estrategico']}")

    print("="*70)

if __name__ == "__main__":
    consolidar_candidatos()
