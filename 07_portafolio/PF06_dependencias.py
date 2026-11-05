"""
PF06_dependencias.py
Grafo de Dependencias entre Proyectos y Orden Topológico de Ejecución
EPS AGUAS DEL SUR S.A. - PETI 2026-2030 (Semana 13)
"""

import os
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

os.environ['MPLCONFIGDIR'] = os.path.join(os.getcwd(), 'scratch_mpl')

def construir_mapa_dependencias():
    df_cand = pd.read_csv("07_portafolio/PF01_portafolio_candidatos.csv")
    aprobados = df_cand[df_cand['estado'] == 'Aprobado']
    
    nombres_dict = dict(zip(aprobados['proyecto_id'], aprobados['nombre']))
    cat_dict = dict(zip(aprobados['proyecto_id'], aprobados['categoria']))

    # Definición de dependencias directas (Predecesor -> Sucesor)
    # El predecesor HABILITA o CONDICIONA la ejecución del sucesor
    dependencias = [
        # PR-11 (Red WAN y Enlaces Redundantes) habilita comunicaciones para SCADA y SOC
        ("PR-11", "PR-02", "Conectividad robusta para telemetría en reservorios"),
        ("PR-11", "PR-09", "Canales seguros para monitoreo SOC en estaciones remotas"),
        
        # PR-12 (Respaldo Inmutable) habilita protección antes de nube y SOC
        ("PR-12", "PR-03", "Copia inmutable base antes de replicación en nube híbrida"),
        ("PR-12", "PR-09", "Línea base de resiliencia ante contingencias de ransomware"),
        
        # PR-06 (Bus ESB / API Gateway) es habilitador estructural de integración
        ("PR-06", "PR-01", "Interconexión de SIGECO con pasarelas de pago y SUNAT"),
        ("PR-06", "PR-04", "Exposición de APIs de consulta y pago para portal/app"),
        ("PR-06", "PR-05", "Interoperabilidad entre catastro comercial y GIS"),
        ("PR-06", "PR-10", "Transmisión automática de parámetros de calidad a SUNASS"),
        
        # PR-07 (Repositorio Maestro MDM y BI) habilita calidad del dato comercial y GIS
        ("PR-07", "PR-01", "Unificación y limpieza del maestro de usuarios/suministros"),
        ("PR-07", "PR-05", "Homologación espacial y catastral de predios y redes"),
        
        # PR-03 (Nube Híbrida y DRP) aloja servicios de alta disponibilidad
        ("PR-03", "PR-01", "Infraestructura elástica para facturación masiva"),
        ("PR-03", "PR-04", "Alojamiento seguro y escalable de plataforma omnicanal"),
        
        # PR-02 (SCADA e IoT) provee telemetría para GIS, CMMS y Calidad de Agua
        ("PR-02", "PR-05", "Capa de telemetría y sensores en tiempo real sobre el GIS"),
        ("PR-02", "PR-08", "Disparo automático de órdenes de trabajo ante fallas de presión"),
        ("PR-02", "PR-10", "Integración de sondas multiparámetro en la red de telemetría"),
        
        # PR-09 (Ciberseguridad) protege la plataforma comercial y transaccional
        ("PR-09", "PR-04", "Bastionado y protección WAF para canal web de pagos")
    ]

    G = nx.DiGraph()

    # Agregar nodos con metadatos
    for pid in aprobados['proyecto_id']:
        G.add_node(pid, label=pid, nombre=nombres_dict[pid], categoria=cat_dict[pid])

    # Agregar aristas
    for u, v, motivo in dependencias:
        G.add_edge(u, v, motivo=motivo)

    # Verificar si es DAG (Grafo Acíclico Dirigido)
    es_dag = nx.is_directed_acyclic_graph(G)
    
    print("="*85)
    print("MAPA DE DEPENDENCIAS Y ANÁLISIS ESTRUCTURAL - EPS AGUAS DEL SUR S.A.")
    print("="*85)
    print(f"¿El grafo de proyectos es acíclico y válido (DAG)?: {'SÍ (Sin dependencias circulares)' if es_dag else 'NO (ERROR: ciclo detectado)'}")
    print(f"Número total de proyectos (nodos): {G.number_of_nodes()}")
    print(f"Número total de dependencias técnicas (aristas): {G.number_of_edges()}")

    # Análisis de proyectos habilitadores (Mayor grado de salida / Out-Degree)
    print("\nPROYECTOS HABILITADORES CLAVE (Prioridad estructural por número de dependientes):")
    out_degrees = sorted(G.out_degree(), key=lambda x: x[1], reverse=True)
    for pid, deg in out_degrees:
        if deg > 0:
            print(f" * [{pid}] {nombres_dict[pid]} -> Habilita a {deg} proyectos ({', '.join(G.successors(pid))})")

    # Orden topológico
    orden_topo = list(nx.topological_sort(G))
    print("\nORDEN TOPOLÓGICO DE EJECUCIÓN (Secuencia que respeta todas las dependencias):")
    for i, pid in enumerate(orden_topo, 1):
        predecesores = list(G.predecessors(pid))
        pred_str = ", ".join(predecesores) if predecesores else "Ninguno (Iniciativa Base)"
        print(f" Paso {i:02d}: [{pid}] {nombres_dict[pid]} | Depende de: {pred_str}")

    print("="*85)

    # 4. Generación gráfica del grafo de dependencias
    plt.figure(figsize=(15, 9))
    
    # Colores por categoría estratégica
    color_map = {
        'Operar': '#4CAF50',      # Verde
        'Crecer': '#2196F3',      # Azul
        'Transformar': '#FF9800'  # Naranja
    }
    node_colors = [color_map[cat_dict[n]] for n in G.nodes()]

    # Posicionamiento estratificado por capas lógicas
    # Capa 0: Bases (PR-11, PR-12)
    # Capa 1: Habilitadores centrales (PR-06, PR-07, PR-09, PR-03)
    # Capa 2: Plataformas operativas/comerciales (PR-02, PR-01)
    # Capa 3: Extensiones y servicios finales (PR-04, PR-05, PR-08, PR-10)
    pos = {
        'PR-11': (0.5, 3.5),
        'PR-12': (0.5, 1.5),
        'PR-06': (2.5, 4.0),
        'PR-07': (2.5, 2.8),
        'PR-09': (2.5, 1.8),
        'PR-03': (2.5, 0.8),
        'PR-02': (4.5, 3.8),
        'PR-01': (4.5, 2.0),
        'PR-10': (6.5, 4.5),
        'PR-08': (6.5, 3.5),
        'PR-05': (6.5, 2.5),
        'PR-04': (6.5, 1.2),
    }

    nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=3200, edgecolors='black', linewidths=1.5)
    nx.draw_networkx_labels(G, pos, font_size=11, font_family='sans-serif', font_weight='bold', font_color='white')

    nx.draw_networkx_edges(G, pos, edge_color='#455A64', arrows=True, arrowsize=22, arrowstyle='-|>', 
                           node_size=3200, connectionstyle='arc3,rad=0.08', width=2.0)

    # Añadir leyenda de categorías
    for cat, col in color_map.items():
        plt.plot([], [], marker='o', color=col, linestyle='None', markersize=12, label=f"Categoría: {cat}")
    
    plt.legend(loc='lower center', bbox_to_anchor=(0.5, -0.05), ncol=3, fontsize=11, frameon=True)
    plt.title('Mapa de Dependencias entre Proyectos y Capas Estructurales\nEPS AGUAS DEL SUR S.A. - PETI 2026-2030', 
              fontsize=14, fontweight='bold', pad=20)
    plt.axis('off')
    plt.tight_layout()

    img_path1 = "07_portafolio/graficos/PF_dependencias.png"
    img_path2 = "evidencias/S13/PF_dependencias.png"
    plt.savefig(img_path1, dpi=300)
    plt.savefig(img_path2, dpi=300)
    plt.close()
    print(f"\n[OK] Grafo exportado en: {img_path1} y {img_path2}")

if __name__ == "__main__":
    construir_mapa_dependencias()
