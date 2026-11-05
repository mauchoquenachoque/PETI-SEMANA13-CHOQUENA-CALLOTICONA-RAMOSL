# Carpeta 07_portafolio · Portafolio de Proyectos de TI
**Organización:** EPS AGUAS DEL SUR S.A.  
**Plan Estratégico de TI (PETI 2026-2030)** — Semana 13  

En esta carpeta reside el desarrollo completo de la **Sección 7.1** del PETI y los artefactos de software que respaldan analítica y financieramente las decisiones del portafolio:

## Contenido de la carpeta:

1. **Documento Principal:**
   * [`7.1_portafolio_de_proyectos.md`](7.1_portafolio_de_proyectos.md): Redacción completa de las subsecciones 7.1.1 a 7.1.8.

2. **Programas de Cálculo y Análisis en Python:**
   * [`PF01_consolidacion.py`](PF01_consolidacion.py): Consolidación de candidatos de las 5 fuentes admisibles y ejecución del control de admisión.
   * [`PF02_tco.py`](PF02_tco.py): Cálculo del Costo Total de Propiedad (TCO a 5 años) y factor TCO/Capex.
   * [`PF04_alternativas.py`](PF04_alternativas.py): Evaluación cuantitativa de 3 alternativas para los 3 proyectos mayores y costo de la inacción.
   * [`PF05_balance.py`](PF05_balance.py): Balance Operar/Crecer/Transformar contrastado con presupuesto actual e industria.
   * [`PF06_dependencias.py`](PF06_dependencias.py): Grafo de dependencias con `networkx`, identificación de habilitadores y orden topológico.
   * [`verificar_cobertura.py`](verificar_cobertura.py): Validación de cobertura de objetivos de la sección 6.2 y reglas de negocio del Paso F.

3. **Archivos de Datos (CSV):**
   * [`PF01_portafolio_candidatos.csv`](PF01_portafolio_candidatos.csv): Listado de 15 candidatos con estado (Aprobado, Fusionado, Retirado).
   * [`PF02_tco.csv`](PF02_tco.csv): Matriz de TCO de los 12 proyectos aprobados con Capex, Opex anual y factores.
   * [`PF04_alternativas.csv`](PF04_alternativas.csv): Matriz de 9 alternativas para los 3 proyectos de mayor inversión con VAN a 5 años.

4. **Fichas Estandarizadas de Proyecto (20 campos):**
   * [`PF03_fichas/`](PF03_fichas/): 12 archivos Markdown (`PR-01.md` al `PR-12.md`).

5. **Gráficos Generados:**
   * [`graficos/PF_balance.png`](graficos/PF_balance.png): Distribución Capex/TCO y contraste con línea base.
   * [`graficos/PF_tco.png`](graficos/PF_tco.png): Inversión inicial vs Opex a 5 años por proyecto.
   * [`graficos/PF_dependencias.png`](graficos/PF_dependencias.png): Grafo de dependencias técnicas y capas arquitectónicas.

