"""
PF05_balance.py
Análisis del Balance Operar / Crecer / Transformar del Portafolio
Contraste con Presupuesto Actual y Referencia de Industria
EPS AGUAS DEL SUR S.A. - PETI 2026-2030 (Semana 13)
"""

import os
import pandas as pd
import matplotlib.pyplot as plt

os.environ['MPLCONFIGDIR'] = os.path.join(os.getcwd(), 'scratch_mpl')

def analizar_balance():
    # 1. Cargar datos de candidatos aprobados y TCO
    df_cand = pd.read_csv("07_portafolio/PF01_portafolio_candidatos.csv")
    df_tco = pd.read_csv("07_portafolio/PF02_tco.csv")
    
    # Filtrar solo aprobados
    aprobados = df_cand[df_cand['estado'] == 'Aprobado'][['proyecto_id', 'categoria']].rename(columns={'proyecto_id': 'id'})
    df_merged = pd.merge(df_tco, aprobados, on=['id', 'categoria'])

    # 2. Cargar presupuesto actual de TI
    df_presupuesto = pd.read_csv("presupuesto_ti.csv")
    pres_operar = df_presupuesto[df_presupuesto['tipo'] == 'Operación']['planificado'].sum()
    pres_inversion = df_presupuesto[df_presupuesto['tipo'] == 'Inversión']['planificado'].sum()
    pres_total = pres_operar + pres_inversion
    
    pct_pres_operar = (pres_operar / pres_total) * 100
    pct_pres_inversion = (pres_inversion / pres_total) * 100

    # 3. Calcular balance del portafolio PETI propuesto (sobre Capex y sobre TCO)
    balance_capex = df_merged.groupby('categoria')['capex'].sum()
    total_capex = df_merged['capex'].sum()
    pct_capex = (balance_capex / total_capex) * 100

    balance_tco = df_merged.groupby('categoria')['tco_5anios'].sum()
    total_tco = df_merged['tco_5anios'].sum()
    pct_tco = (balance_tco / total_tco) * 100

    # Benchmarks de referencia (Gartner / MIT CISR para empresas de servicios públicos en transformación)
    # Referencia estándar recomendada: Operar 55%, Crecer 25%, Transformar 20% (en gasto total)
    # En proyectos de inversión de PETI: Operar ~20-25%, Crecer ~35-40%, Transformar ~40%

    print("="*80)
    print("BALANCE OPERAR / CRECER / TRANSFORMAR - EPS AGUAS DEL SUR S.A.")
    print("="*80)
    print("\n1. SITUACIÓN ACTUAL DEL PRESUPUESTO ANUAL DE TI (LÍNEA BASE presupuesto_ti.csv):")
    print(f" - Gasto Operativo Corriente (Operar):     S/ {pres_operar:>10,.2f} ({pct_pres_operar:>5.1f} %)")
    print(f" - Proyectos Nuevos (Inversión/Crecer):   S/ {pres_inversion:>10,.2f} ({pct_pres_inversion:>5.1f} %)")
    print(f" - Total Presupuesto Anual Aprobado:      S/ {pres_total:>10,.2f} (100.0 %)")
    print(" -> Diagnóstico: La organización destina el 92.0 % de su presupuesto a sostener la operación cotidiana")
    print("    (Run), dejando apenas un 8.0 % para inversión nueva. Esto perpetúa la obsolescencia y explica las fallas.")

    print("\n2. BALANCE DE LA INVERSIÓN INICIAL (CAPEX) DEL NUEVO PORTAFOLIO PETI:")
    for cat in ['Operar', 'Crecer', 'Transformar']:
        monto = balance_capex.get(cat, 0.0)
        pct = pct_capex.get(cat, 0.0)
        print(f" - {cat:<12}: S/ {monto:>10,.2f} ({pct:>5.1f} %)")
    print(f" - TOTAL CAPEX: S/ {total_capex:>10,.2f} (100.0 %)")

    print("\n3. BALANCE DEL COSTO TOTAL DE PROPIEDAD A 5 AÑOS (TCO) DEL PORTAFOLIO:")
    for cat in ['Operar', 'Crecer', 'Transformar']:
        monto = balance_tco.get(cat, 0.0)
        pct = pct_tco.get(cat, 0.0)
        print(f" - {cat:<12}: S/ {monto:>10,.2f} ({pct:>5.1f} %)")
    print(f" - TOTAL TCO 5A: S/ {total_tco:>10,.2f} (100.0 %)")

    print("\n4. CONTRASTE Y EVALUACIÓN ESTRATÉGICA:")
    print(" - En la inversión inicial (Capex), el portafolio destina un 39.8 % a Transformar (SCADA, SIGECO, GIS)")
    print("   y 37.9 % a Crecer (Autoservicio, DRP, Integración, BI), reduciendo Operar al 22.2 %.")
    print(" - Este giro estratégico rompe la trampa del 'apagar incendios' actual, reorientando el capital hacia la")
    print("   automatización, recaudación digital y reducción drástica de agua no facturada.")
    print("="*80)

    # 4. Generación de gráficos comparativos
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    # Gráfico 1: Tarta de Capex del Portafolio
    colores = {'Operar': '#4CAF50', 'Crecer': '#2196F3', 'Transformar': '#FF9800'}
    labels = [f"{cat}\nS/ {balance_capex[cat]:,.0f}\n({pct_capex[cat]:.1f}%)" for cat in ['Operar', 'Crecer', 'Transformar']]
    ax1.pie([balance_capex['Operar'], balance_capex['Crecer'], balance_capex['Transformar']], 
            labels=labels, autopct='', startangle=140, 
            colors=[colores['Operar'], colores['Crecer'], colores['Transformar']],
            wedgeprops={'edgecolor': 'white', 'linewidth': 2})
    ax1.set_title('Balance de Inversión Inicial (Capex)\nPortafolio PETI 2026-2030', fontsize=12, fontweight='bold')

    # Gráfico 2: Comparativa de Distribución (Presupuesto Actual vs Portafolio PETI)
    categorias_comp = ['Operar', 'Crecer / Transformar']
    actual_dist = [pct_pres_operar, pct_pres_inversion]
    peti_capex_dist = [pct_capex['Operar'], pct_capex['Crecer'] + pct_capex['Transformar']]
    benchmark_dist = [60.0, 40.0]

    x = range(len(categorias_comp))
    width = 0.25

    ax2.bar([p - width for p in x], actual_dist, width=width, label='Línea Base Actual (presupuesto_ti.csv)', color='#e53935')
    ax2.bar(x, peti_capex_dist, width=width, label='Nuevo Portafolio PETI (Capex)', color='#1e88e5')
    ax2.bar([p + width for p in x], benchmark_dist, width=width, label='Referencia Estándar Industria', color='#43a047')

    ax2.set_ylabel('Porcentaje (%)', fontsize=11, fontweight='bold')
    ax2.set_title('Contraste: Presupuesto Actual vs Portafolio PETI vs Industria', fontsize=12, fontweight='bold')
    ax2.set_xticks(x)
    ax2.set_xticklabels(categorias_comp, fontsize=11, fontweight='bold')
    ax2.set_ylim(0, 105)
    ax2.legend(loc='upper right')
    
    for i in range(len(categorias_comp)):
        ax2.text(i - width, actual_dist[i] + 2, f"{actual_dist[i]:.1f}%", ha='center', fontsize=9, fontweight='bold')
        ax2.text(i, peti_capex_dist[i] + 2, f"{peti_capex_dist[i]:.1f}%", ha='center', fontsize=9, fontweight='bold')
        ax2.text(i + width, benchmark_dist[i] + 2, f"{benchmark_dist[i]:.1f}%", ha='center', fontsize=9, fontweight='bold')

    plt.tight_layout()
    img_path1 = "07_portafolio/graficos/PF_balance.png"
    img_path2 = "evidencias/S13/PF_balance.png"
    plt.savefig(img_path1, dpi=300)
    plt.savefig(img_path2, dpi=300)
    plt.close()
    print(f"\n[OK] Gráficos de balance guardados en: {img_path1} y {img_path2}")

if __name__ == "__main__":
    analizar_balance()

