"""
PF02_tco.py
Cálculo del Costo Total de Propiedad (TCO) a 5 Años y Factor TCO/Inversión
EPS AGUAS DEL SUR S.A. - PETI 2026-2030 (Semana 13)
"""

import os
import pandas as pd
import matplotlib.pyplot as plt

os.environ['MPLCONFIGDIR'] = os.path.join(os.getcwd(), 'scratch_mpl')

def calcular_tco():
    proyectos_tco = [
        {
            "id": "PR-01",
            "nombre": "SIGECO-Agua (Gestión Comercial y Facturación)",
            "categoria": "Transformar",
            "capex": 380000.0,
            "incertidumbre_capex": "±15%",
            "opex_anual": 65000.0,
            "justificacion_opex": "Soporte N2/N3, actualización de reglas tributarias SUNAT, mantenimiento de base de datos comercial y hosting transaccional."
        },
        {
            "id": "PR-02",
            "nombre": "SCADA e Infraestructura IoT de Telemetría",
            "categoria": "Transformar",
            "capex": 420000.0,
            "incertidumbre_capex": "±20%",
            "opex_anual": 72000.0,
            "justificacion_opex": "Mantenimiento preventivo/calibración de sensores y RTU en reservorios, repuestos de instrumentación y enlaces de telemetría."
        },
        {
            "id": "PR-03",
            "nombre": "Nube Híbrida, Datacenter Contingencia y DRP",
            "categoria": "Crecer",
            "capex": 290000.0,
            "incertidumbre_capex": "±15%",
            "opex_anual": 75000.0,
            "justificacion_opex": "Suscripción IaaS en nube híbrida para replicación activa, enlaces dedicados de contingencia y pruebas anuales de conmutación DRP."
        },
        {
            "id": "PR-04",
            "nombre": "Plataforma Omnicanal de Autoservicio y Atención",
            "categoria": "Crecer",
            "capex": 160000.0,
            "incertidumbre_capex": "±15%",
            "opex_anual": 42000.0,
            "justificacion_opex": "API oficial de WhatsApp Business, pasarela de cobro digital (comisiones bancarias fijas), hosting y soporte de app móvil."
        },
        {
            "id": "PR-05",
            "nombre": "GIS Corporativo para Redes de Agua y Alcantarillado",
            "categoria": "Transformar",
            "capex": 240000.0,
            "incertidumbre_capex": "±20%",
            "opex_anual": 48000.0,
            "justificacion_opex": "Mantenimiento del servidor cartográfico, actualización de ortofotos satelitales, licencias de visualización y soporte geográfico."
        },
        {
            "id": "PR-06",
            "nombre": "Bus de Integración ESB / API Gateway e Interoperabilidad",
            "categoria": "Crecer",
            "capex": 150000.0,
            "incertidumbre_capex": "±15%",
            "opex_anual": 35000.0,
            "justificacion_opex": "Soporte empresarial del runtime de integración, monitoreo de latencia y gestión de certificados digitales para PIDE/SUNASS."
        },
        {
            "id": "PR-07",
            "nombre": "Repositorio Maestro MDM, Gobierno del Dato y BI",
            "categoria": "Crecer",
            "capex": 180000.0,
            "incertidumbre_capex": "±15%",
            "opex_anual": 38000.0,
            "justificacion_opex": "Suscripciones de visualización analítica, mantenimiento y optimización de pipelines de datos y auditoría de calidad de datos."
        },
        {
            "id": "PR-08",
            "nombre": "CMMS / GMAO Mantenimiento de Activos y Redes",
            "categoria": "Operar",
            "capex": 140000.0,
            "incertidumbre_capex": "±15%",
            "opex_anual": 32000.0,
            "justificacion_opex": "Licenciamiento concurrente para cuadrillas en campo, soporte técnico de la app móvil y actualización de catálogos de fallas."
        },
        {
            "id": "PR-09",
            "nombre": "Ciberseguridad Redes OT/IT y Centro SOC",
            "categoria": "Operar",
            "capex": 190000.0,
            "incertidumbre_capex": "±15%",
            "opex_anual": 55000.0,
            "justificacion_opex": "Servicio gestionado de monitoreo SOC 24/7, suscripción de firmas EDR e inteligencia de amenazas para redes industriales SCADA."
        },
        {
            "id": "PR-10",
            "nombre": "Monitoreo Automatizado de Calidad de Agua",
            "categoria": "Crecer",
            "capex": 210000.0,
            "incertidumbre_capex": "±20%",
            "opex_anual": 45000.0,
            "justificacion_opex": "Reposición de reactivos químicos patrón, calibración semestral certificada INACAL de electrodos y sondas en plantas."
        },
        {
            "id": "PR-11",
            "nombre": "Red WAN y Enlaces Redundantes Estaciones Remotas",
            "categoria": "Operar",
            "capex": 130000.0,
            "incertidumbre_capex": "±15%",
            "opex_anual": 52000.0,
            "justificacion_opex": "Abonos mensuales de enlaces dedicados corporativos y enlaces satelitales de respaldo Starlink en plantas de captación y reservorios."
        },
        {
            "id": "PR-12",
            "nombre": "Sistema de Respaldo Inmutable Anti-Ransomware",
            "categoria": "Operar",
            "capex": 120000.0,
            "incertidumbre_capex": "±15%",
            "opex_anual": 30000.0,
            "justificacion_opex": "Mantenimiento preventivo del hardware de almacenamiento inmutable WORM y suscripción a bóveda externa en nube segura."
        }
    ]

    df = pd.DataFrame(proyectos_tco)
    df['opex_5anios'] = df['opex_anual'] * 5.0
    df['tco_5anios'] = df['capex'] + df['opex_5anios']
    df['factor_tco_inversion'] = (df['tco_5anios'] / df['capex']).round(2)

    csv_path = "07_portafolio/PF02_tco.csv"
    df.to_csv(csv_path, index=False, encoding="utf-8-sig")
    print(f"[OK] Archivo TCO exportado: {csv_path}")

    # Impresión de resultados
    print("\n" + "="*85)
    print("MATRIZ DE COSTO TOTAL DE PROPIEDAD (TCO A 5 AÑOS) - EPS AGUAS DEL SUR S.A.")
    print("="*85)
    print(f"{'ID':<6} {'Proyecto':<35} {'Capex (S/)':<12} {'Opex Anual':<12} {'TCO 5A (S/)':<14} {'Factor':<6}")
    print("-" * 85)
    for _, r in df.iterrows():
        print(f"{r['id']:<6} {r['nombre'][:34]:<35} {r['capex']:>10,.2f} {r['opex_anual']:>10,.2f} {r['tco_5anios']:>12,.2f} {r['factor_tco_inversion']:>6.2f}x")
    print("-" * 85)
    
    tot_capex = df['capex'].sum()
    tot_opex_anual = df['opex_anual'].sum()
    tot_opex_5a = df['opex_5anios'].sum()
    tot_tco = df['tco_5anios'].sum()
    factor_global = tot_tco / tot_capex

    print(f"{'TOTAL':<6} {'PORTAFOLIO (12 PROYECTOS)':<35} {tot_capex:>10,.2f} {tot_opex_anual:>10,.2f} {tot_tco:>12,.2f} {factor_global:>6.2f}x")
    print("="*85)

    print("\nINTERPRETACIÓN DEL FACTOR TCO / INVERSIÓN INICIAL:")
    print(f"1. El factor global del portafolio es de {factor_global:.2f}x. Esto demuestra que por cada sol invertido en Capex inicial,")
    print(f"   la empresa deberá destinar S/ {(factor_global - 1):.2f} adicionales en gastos operativos y de mantenimiento durante los primeros 5 años.")
    print("2. Proyectos con mayor factor TCO/Inversión:")
    top_factor = df.sort_values('factor_tco_inversion', ascending=False).head(3)
    for _, r in top_factor.iterrows():
        print(f"   * [{r['id']}] {r['nombre']}: Factor = {r['factor_tco_inversion']:.2f}x (Capex: S/ {r['capex']:,.0f} vs Opex 5A: S/ {r['opex_5anios']:,.0f})")
    print("   -> Explicación: PR-11 (Red WAN y enlaces) y PR-09 (Ciberseguridad) dependen intensivamente de servicios de conectividad y SOC")
    print("      gestionado mensualizados, por lo que su costo recurrente supera ampliamente la inversión inicial en hardware.")

    print("\nPROYECTOS DE MAYOR INVERSIÓN INICIAL (CANDIDATOS A CASOS DE NEGOCIO):")
    top_capex = df.sort_values('capex', ascending=False).head(3)
    for _, r in top_capex.iterrows():
        print(f"   * [{r['id']}] {r['nombre']}: Capex = S/ {r['capex']:,.2f} | TCO = S/ {r['tco_5anios']:,.2f}")

    # Generar gráfico comparativo TCO (Capex vs Opex 5 años)
    plt.figure(figsize=(12, 6))
    df_plot = df.sort_values('tco_5anios', ascending=True)
    y_pos = range(len(df_plot))
    
    plt.barh(y_pos, df_plot['capex'], label='Inversión Inicial (Capex)', color='#1f77b4')
    plt.barh(y_pos, df_plot['opex_5anios'], left=df_plot['capex'], label='Costo Operativo a 5 Años (Opex)', color='#ff7f0e')
    
    plt.yticks(y_pos, df_plot['id'] + ': ' + df_plot['nombre'].str[:30])
    plt.xlabel('Soles (PEN)', fontsize=11, fontweight='bold')
    plt.title('Costo Total de Propiedad (TCO a 5 Años) por Proyecto - EPS AGUAS DEL SUR S.A.', fontsize=12, fontweight='bold')
    plt.legend(loc='lower right')
    plt.tight_layout()
    
    img_path1 = "07_portafolio/graficos/PF_tco.png"
    img_path2 = "evidencias/S13/PF_tco.png"
    plt.savefig(img_path1, dpi=300)
    plt.savefig(img_path2, dpi=300)
    plt.close()
    print(f"\n[OK] Gráfico generado en: {img_path1} y {img_path2}")

if __name__ == "__main__":
    calcular_tco()
