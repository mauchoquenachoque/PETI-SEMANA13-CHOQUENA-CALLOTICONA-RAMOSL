"""
PF04_alternativas.py
Casos de Negocio, Comparación de Alternativas y Costo de la Inacción
EPS AGUAS DEL SUR S.A. - PETI 2026-2030 (Semana 13)
"""

import pandas as pd
import os

def generar_casos_negocio():
    alternativas = [
        # --- PROYECTO 1: PR-02 SCADA e IoT de Telemetría (Capex: S/ 420,000) ---
        {
            "proyecto_id": "PR-02",
            "proyecto_nombre": "Plataforma SCADA e Infraestructura IoT de Telemetría",
            "alternativa_id": "ALT-02-0",
            "nombre_alternativa": "Alternativa 0: No hacer nada (Status Quo)",
            "capex": 0.0,
            "opex_anual": 115000.0,
            "tco_5anios": 575000.0,
            "beneficio_anual": -320000.0,  # Costo de la inacción
            "beneficio_5anios": -1600000.0,
            "van_5anios": -2175000.0,
            "es_recomendada": "No",
            "descripcion": "Mantener medición manual y cuadrillas viajando a reservorios. Pérdida continua por fugas no detectadas (38% agua no facturada), sobrecosto de energía en bombeo y multas SUNASS por corte intempestivo.",
            "costo_inaccion_cuantificado": "S/ 320,000 anuales (S/ 180,000 en pérdidas de agua potable bombeada, S/ 85,000 en horas extra de cuadrillas nocturnas y S/ 55,000 en sanciones SUNASS)."
        },
        {
            "proyecto_id": "PR-02",
            "proyecto_nombre": "Plataforma SCADA e Infraestructura IoT de Telemetría",
            "alternativa_id": "ALT-02-1",
            "nombre_alternativa": "Alternativa 1 (Recomendada): SCADA Modular Abierto e IoT Industrial (MQTT/LoRaWAN)",
            "capex": 420000.0,
            "opex_anual": 72000.0,
            "tco_5anios": 780000.0,
            "beneficio_anual": 410000.0,
            "beneficio_5anios": 2050000.0,
            "van_5anios": 1270000.0,
            "es_recomendada": "Sí",
            "descripcion": "Sensores IoT multipunto en reservorios y macrosectores con concentradores LoRaWAN y plataforma SCADA basada en Ignition/SCADA-LTS. Detección automática de roturas y control de presión.",
            "costo_inaccion_cuantificado": "Elimina el 85% de las pérdidas por roturas no visibles y reduce el costo de bombeo en un 18%."
        },
        {
            "proyecto_id": "PR-02",
            "proyecto_nombre": "Plataforma SCADA e Infraestructura IoT de Telemetría",
            "alternativa_id": "ALT-02-2",
            "nombre_alternativa": "Alternativa 2: Sistema SCADA Propietario Monolítico Llave en Mano",
            "capex": 680000.0,
            "opex_anual": 125000.0,
            "tco_5anios": 1305000.0,
            "beneficio_anual": 390000.0,
            "beneficio_5anios": 1950000.0,
            "van_5anios": 645000.0,
            "es_recomendada": "No",
            "descripcion": "Adquisición de paquete propietario cerrado de fabricante multinacional. Alto costo de licencias por tag/variable y dependencia tecnológica (vendor lock-in) severa.",
            "costo_inaccion_cuantificado": "N/A (Evita la inacción pero con sobrecosto del 67% sobre la alternativa recomendada)."
        },

        # --- PROYECTO 2: PR-01 SIGECO-Agua (Capex: S/ 380,000) ---
        {
            "proyecto_id": "PR-01",
            "proyecto_nombre": "SIGECO-Agua (Gestión Comercial y Facturación Electrónica)",
            "alternativa_id": "ALT-01-0",
            "nombre_alternativa": "Alternativa 0: No hacer nada (Status Quo)",
            "capex": 0.0,
            "opex_anual": 98000.0,
            "tco_5anios": 490000.0,
            "beneficio_anual": -290000.0,  # Costo de la inacción
            "beneficio_5anios": -1450000.0,
            "van_5anios": -1940000.0,
            "es_recomendada": "No",
            "descripcion": "Continuar con sistema cliente-servidor obsoleto en FoxPro/VB6. Errores recurrentes en lectura de micromedición, demoras de 12 días en emisión de recibos y contingencias con SUNAT.",
            "costo_inaccion_cuantificado": "S/ 290,000 anuales (S/ 140,000 en facturación rezagada e incobrable, S/ 90,000 en soporte correctivo de emergencia y S/ 60,000 por no integración con pasarelas bancarias)."
        },
        {
            "proyecto_id": "PR-01",
            "proyecto_nombre": "SIGECO-Agua (Gestión Comercial y Facturación Electrónica)",
            "alternativa_id": "ALT-01-1",
            "nombre_alternativa": "Alternativa 1 (Recomendada): Plataforma Web/Móvil Especializada en Utilities con API de Facturación SUNAT",
            "capex": 380000.0,
            "opex_anual": 65000.0,
            "tco_5anios": 705000.0,
            "beneficio_anual": 385000.0,
            "beneficio_5anios": 1925000.0,
            "van_5anios": 1220000.0,
            "es_recomendada": "Sí",
            "descripcion": "Implementación de solución comercial modular en arquitectura cloud-native, con toma de lectura móvil con fotografía georreferenciada y facturación electrónica instantánea.",
            "costo_inaccion_cuantificado": "Aumenta la efectividad de recaudación del 84% al 96% y reduce el ciclo de cobranza de 42 a 18 días."
        },
        {
            "proyecto_id": "PR-01",
            "proyecto_nombre": "SIGECO-Agua (Gestión Comercial y Facturación Electrónica)",
            "alternativa_id": "ALT-01-2",
            "nombre_alternativa": "Alternativa 2: Desarrollo a Medida In-House desde Cero",
            "capex": 490000.0,
            "opex_anual": 80000.0,
            "tco_5anios": 890000.0,
            "beneficio_anual": 310000.0,
            "beneficio_5anios": 1550000.0,
            "van_5anios": 660000.0,
            "es_recomendada": "No",
            "descripcion": "Contratación de equipo de programadores externos para desarrollar un sistema desde cero. Plazo incierto (> 24 meses), alto riesgo de desviación como ocurrió en el Expediente 1.",
            "costo_inaccion_cuantificado": "N/A (Riesgo severo de sobrecosto y retraso en cumplimiento de metas regulatorias SUNASS)."
        },

        # --- PROYECTO 3: PR-03 Nube Híbrida y DRP (Capex: S/ 290,000) ---
        {
            "proyecto_id": "PR-03",
            "proyecto_nombre": "Nube Híbrida, Datacenter de Contingencia y DRP",
            "alternativa_id": "ALT-03-0",
            "nombre_alternativa": "Alternativa 0: No hacer nada (Status Quo)",
            "capex": 0.0,
            "opex_anual": 85000.0,
            "tco_5anios": 425000.0,
            "beneficio_anual": -240000.0,  # Costo de la inacción
            "beneficio_5anios": -1200000.0,
            "van_5anios": -1625000.0,
            "es_recomendada": "No",
            "descripcion": "Servidor único en sede central sin contingencia física ni en nube (problema no resuelto del Expediente 2). Riesgo inminente de detención total por desastre sísmico o ransomware.",
            "costo_inaccion_cuantificado": "S/ 240,000 anuales esperados (Costo ponderado de caída del servicio comercial y operacional durante 5 días hábiles, pérdidas de recaudación y penalidades)."
        },
        {
            "proyecto_id": "PR-03",
            "proyecto_nombre": "Nube Híbrida, Datacenter de Contingencia y DRP",
            "alternativa_id": "ALT-03-1",
            "nombre_alternativa": "Alternativa 1 (Recomendada): Esquema Híbrido Activo-Pasivo en Nube Pública Segura",
            "capex": 290000.0,
            "opex_anual": 75000.0,
            "tco_5anios": 665000.0,
            "beneficio_anual": 280000.0,
            "beneficio_5anios": 1400000.0,
            "van_5anios": 735000.0,
            "es_recomendada": "Sí",
            "descripcion": "Consolidación de infraestructura on-premise local hiperconvergente replicada de forma continua hacia nube pública de nivel Tier III (AWS/Azure) con RPO < 15 min y RTO < 2 horas.",
            "costo_inaccion_cuantificado": "Garantiza disponibilidad 99.85% y protege el patrimonio de información crítico de la EPS ante cualquier contingencia."
        },
        {
            "proyecto_id": "PR-03",
            "proyecto_nombre": "Nube Híbrida, Datacenter de Contingencia y DRP",
            "alternativa_id": "ALT-03-2",
            "nombre_alternativa": "Alternativa 2: Construcción de Segundo Datacenter Físico Propio en Planta Calana",
            "capex": 580000.0,
            "opex_anual": 110000.0,
            "tco_5anios": 1130000.0,
            "beneficio_anual": 270000.0,
            "beneficio_5anios": 1350000.0,
            "van_5anios": 220000.0,
            "es_recomendada": "No",
            "descripcion": "Acondicionamiento civil, grupo electrógeno, climatización de precisión y servidores duplicados en planta remota. Costo de capital desproporcionado para el tamaño de la EPS.",
            "costo_inaccion_cuantificado": "N/A (Inversión innecesaria en infraestructura física pasiva en zona de alto riesgo telúrico)."
        }
    ]

    df_alt = pd.DataFrame(alternativas)
    csv_path = "07_portafolio/PF04_alternativas.csv"
    df_alt.to_csv(csv_path, index=False, encoding="utf-8-sig")
    print(f"[OK] Archivo generado exitosamente: {csv_path}")

    print("\n" + "="*95)
    print("CASOS DE NEGOCIO: COMPARACIÓN DE ALTERNATIVAS Y COSTO DE LA INACCIÓN")
    print("EPS AGUAS DEL SUR S.A. - 3 PROYECTOS DE MAYOR INVERSIÓN")
    print("="*95)
    
    for pid in ["PR-02", "PR-01", "PR-03"]:
        sub = df_alt[df_alt['proyecto_id'] == pid]
        p_nombre = sub.iloc[0]['proyecto_nombre']
        print(f"\n>>> PROYECTO: [{pid}] {p_nombre}")
        print(f"{'Alternativa':<32} {'Capex (S/)':<12} {'TCO 5A':<12} {'Benef. 5A':<14} {'VAN 5A':<12} {'¿Recomendada?'}")
        print("-" * 95)
        for _, r in sub.iterrows():
            print(f"{r['nombre_alternativa'][:30]:<32} {r['capex']:>10,.2f} {r['tco_5anios']:>10,.2f} {r['beneficio_5anios']:>12,.2f} {r['van_5anios']:>10,.2f} {r['es_recomendada']:^14}")
        
        alt0 = sub[sub['alternativa_id'].str.endswith('-0')].iloc[0]
        alt1 = sub[sub['es_recomendada'] == 'Sí'].iloc[0]
        print(f" -> COSTO CUANTIFICADO DE LA INACCIÓN (ALT 0): {alt0['costo_inaccion_cuantificado']}")
        print(f" -> DICTAMEN: Se recomienda formalmente '{alt1['nombre_alternativa']}' con un VAN a 5 años de S/ {alt1['van_5anios']:,.2f}.")
    
    print("\n" + "="*95)

if __name__ == "__main__":
    generar_casos_negocio()

