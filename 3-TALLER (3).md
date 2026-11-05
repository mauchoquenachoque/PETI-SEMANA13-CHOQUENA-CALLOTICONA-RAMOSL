[Semana 13](README.md) · [Teoría](1-TEORIA.md) · [Dinámica de aula](2-DINAMICA.md) · **Taller de laboratorio**

# Semana 13

## Construcción del portafolio de proyectos

**SI-886 - Planeamiento Estratégico de TI** - Sesión 2 en laboratorio - **Taller grupal** · calificación **procedimental**

> ¿Un término no le resulta claro? Está definido en el [glosario técnico del curso](../GLOSARIO.md).

---

## Qué entregas

| | |
|---|---|
| **Archivo** | `SI886-S13-TALLER-Grupo<N>.pdf` |
| **Modalidad** | **Taller grupal.** Un informe por equipo, con los códigos de todos los integrantes. El repositorio y el PETI son del equipo |
| **Plantilla obligatoria** | [SI886-PLANTILLA-TALLER.docx](../PLANTILLAS/SI886-PLANTILLA-TALLER.docx) |
| **Formato** | PDF exportado desde la plantilla en Word, con la carátula de la UPT, el índice actualizado y las capturas numeradas |
| **Qué va dentro** | Las secciones de la plantilla. La sección **5. Resultados y evidencias** de la plantilla se llena con la lista de comprobación 3.2 de esta guía, una fila por resultado, y **cada resultado necesita la evidencia que lo demuestre**. No se copian de aquí los objetivos, la duración ni los resultados de aprendizaje |
| **Dónde se sube** | Aula virtual, tarea «Taller · Semana 13» |
| **Cuándo vence** | Según lo programado en el aula virtual |

> No se califica un informe entregado en `.docx`, sin carátula, sin los códigos de los integrantes o con resultados declarados sin evidencia.

---

## 1. Información sobre el evento práctico

### 1.1. Objetivos

- Consolidar los **candidatos a proyecto** provenientes de las cinco fuentes admisibles.
- **Depurar** el portafolio. Fusionar duplicados y descartar los no trazables.
- Elaborar la **ficha estandarizada** de cada proyecto.
- Calcular el **TCO a cinco años** de cada proyecto.
- Desarrollar el **caso de negocio** de los tres proyectos de mayor inversión.
- Evaluar el **impacto de cada proyecto en el desarrollo sostenible**, sobre las cinco dimensiones.
- Analizar el **balance operar/crecer/transformar** del portafolio.
- Construir el **mapa de dependencias** entre proyectos.
- Redactar la **Sección 7.1** del PETI (Plan Estratégico de Tecnologías de Información).

**Tecnología que aplica el estudiante en este taller**

| Tecnología | Qué hace con ella | Dónde queda la evidencia |
|---|---|---|
| **pandas** | Consolida candidatos desde cinco fuentes, calcula el TCO a cinco años, compara alternativas y mide el balance operar/crecer/transformar | `PF01`, `PF02`, `PF04`, `PF_balance.png` |
| **networkx** | Construye el grafo de dependencias entre proyectos y obtiene el orden topológico | `PF_dependencias.png`, salida de `PF06` |
| **matplotlib** | Grafica balance, TCO por proyecto y mapa de dependencias | `graficos/` |
| **Markdown** estructurado | Redacta una ficha de proyecto de 20 campos por proyecto, versionable | `PF03_fichas/PR-NN.md` |

### 1.2. Recursos

| Recurso | Detalle |
|---|---|
| **[`RECURSOS-TALLER/`](RECURSOS-TALLER/)** | Documentos del caso de su organización y programas de este taller, listos para copiar. El [README](RECURSOS-TALLER/README.md) de la carpeta explica cada archivo |
| Secciones Sección 3.5, Sección 4.1.5, Sección 4.3.5, Sección 5.4.2 y Sección 6.1.7 del PETI | Las cinco fuentes admisibles |
| **PMBOK Guide** / **ISO 21500** | Estructura del caso de negocio |
| **Python 3.11+** con `pandas`, `matplotlib`, `networkx` | Consolidación, TCO y grafo de dependencias |
| **LibreOffice Calc** | Fichas y TCO |
| **draw.io** | Mapa de dependencias |
| Cotizaciones referenciales | Precios de mercado para estimar; se documenta la fuente |

### 1.3. Seguridad

1. El portafolio contiene **cifras de inversión** de la organización. Información **Confidencial**.
2. Las estimaciones de costo se basan en referencias de mercado documentadas o en la experiencia de la organización; **se declara siempre el origen y el margen de incertidumbre** de cada estimación.
3. No se solicitan cotizaciones formales a proveedores en nombre de la organización sin su autorización expresa.
4. Las cifras se presentan con su **rango**, no como valor exacto. Una estimación presentada como cifra cerrada compromete al equipo formulador con una precisión que no tiene.

---

## 2. Procedimiento o Metodología

> **Recursos de este taller.** Están en [`RECURSOS-TALLER/`](RECURSOS-TALLER/) y su [README](RECURSOS-TALLER/README.md) explica cada archivo. Su equipo usa la subcarpeta de su organización, `RECURSOS-TALLER/EMPRESA-<NN>-<nombre>/`. Trae `expedientes-de-inversion.md` (los tres expedientes de inversiones cerradas, con su caso de negocio y su beneficio declarado), `inversiones_cerradas.csv`, `presupuesto_ti.csv` y `pagos.csv`. Los expedientes muestran cómo decide hoy la organización sus inversiones y son la línea base del modelo que el portafolio propone; el presupuesto da el balance actual operar/crecer/transformar que la sección 7.1.6 contrasta; los pagos permiten estimar el gasto real en proveedores de TI para el costo operativo del TCO.
>
> **Las tablas de ejemplo de esta guía**, y los datos que traen los programas, están resueltas sobre Distribuidora Andina del Sur S.A.C., el caso de respaldo del curso descrito en [`ANEXO-CASO-SIMULADO.md`](../ANEXO-CASO-SIMULADO.md). Muestran el formato y el nivel de detalle que se espera. Las cifras de su informe salen de su organización, no de estas tablas.

> **Cómo leer los pasos.** Cada paso nombra el archivo que el equipo crea, con su ruta dentro del repositorio del PETI, por ejemplo `07_portafolio/PF03_fichas/PR-01.md`. La carpeta es la de la sección del plan, dentro de la estructura de carpetas del repositorio; el nombre es el que usan los programas y la lista de comprobación. La tabla o la plantilla que sigue a la ruta es **el contenido de ese archivo**. Ese mismo archivo, versionado en GitHub, es la evidencia que se enlaza en el informe.

### Paso A — Consolidar y depurar los candidatos

**Programa [`PF01_consolidacion.py`](RECURSOS-TALLER/PF01_consolidacion.py).** No lee ningún archivo: los candidatos se escriben dentro del programa. Produce `PF01_portafolio_candidatos.csv`. Se copia a `07_portafolio/` del repositorio del equipo y **se edita con los datos de su organización**: el programa hace el cálculo, las cifras y su justificación son del equipo.

```bash
# desde la raíz del repositorio del equipo; <curso> es la carpeta del material del curso
cp <curso>/SEMANA-13/RECURSOS-TALLER/PF01_consolidacion.py 07_portafolio/
cd 07_portafolio && python3 PF01_consolidacion.py
```

**Depuración.** Se fusionan candidatos que comparten alcance (por ejemplo C-05 puede ser un entregable de C-04) y se documenta cada fusión con su razón.

### Paso B — Ficha estandarizada y TCO

**Programa [`PF02_tco.py`](RECURSOS-TALLER/PF02_tco.py).** No lee ningún archivo: los costos por proyecto se escriben dentro del programa. Produce `PF02_tco.csv`. Se copia a `07_portafolio/` del repositorio del equipo y **se edita con los datos de su organización**: el programa hace el cálculo, las cifras y su justificación son del equipo.

```bash
# desde la raíz del repositorio del equipo; <curso> es la carpeta del material del curso
cp <curso>/SEMANA-13/RECURSOS-TALLER/PF02_tco.py 07_portafolio/
cd 07_portafolio && python3 PF02_tco.py
```

**Ficha por proyecto**, archivo `07_portafolio/PF03_fichas/PR-01.md` del repositorio del equipo, con los 20 campos de la sección 1.4.

### Paso C — Casos de negocio de los tres mayores

Para los tres proyectos de mayor TCO se desarrolla el caso de negocio completo, con las tres alternativas:

**Programa [`PF04_alternativas.py`](RECURSOS-TALLER/PF04_alternativas.py).** No lee ningún archivo: las alternativas se escriben dentro del programa. Produce `PF04_alternativas.csv`. Se copia a `07_portafolio/` del repositorio del equipo y **se edita con los datos de su organización**: el programa hace el cálculo, las cifras y su justificación son del equipo.

```bash
# desde la raíz del repositorio del equipo; <curso> es la carpeta del material del curso
cp <curso>/SEMANA-13/RECURSOS-TALLER/PF04_alternativas.py 07_portafolio/
cd 07_portafolio && python3 PF04_alternativas.py
```

> **La alternativa «no hacer nada» tiene beneficio negativo**, que representa el costo de la inacción. Es la cifra más persuasiva del caso de negocio y la que la mayoría de los planes omite.

**Impacto en el desarrollo sostenible.** Cada caso de negocio lleva esta tabla. Es lo que la Semana 16 consolidará, y **una dimensión que no aplica se declara y se explica**, no se deja vacía.

| Dimensión | A quién afecta | Efecto esperado, con su cifra o su indicador | ¿Norma o derecho aplicable? |
|---|---|---|---|
| **Sociedad** | | | |
| **Economía** | | | |
| **Salud y seguridad** | | | |
| **Marco legal** | | | |
| **Medio ambiente** | | | |

> **La prueba.** «Beneficiará a la comunidad» no cuenta. «Reduce de 12 a 5 días el trámite que hoy hacen 1 200 vecinos al año, y les evita dos traslados presenciales» sí cuenta.

### Paso D — Balance del portafolio y dependencias

**Programa [`PF05_balance.py`](RECURSOS-TALLER/PF05_balance.py).** Lee `PF01_portafolio_candidatos.csv` y `PF02_tco.csv`. Produce el balance en pantalla y `graficos/PF_balance.png`. Se copia a `07_portafolio/` del repositorio del equipo y **se edita con los datos de su organización**: el programa hace el cálculo, las cifras y su justificación son del equipo.

```bash
# desde la raíz del repositorio del equipo; <curso> es la carpeta del material del curso
cp <curso>/SEMANA-13/RECURSOS-TALLER/PF05_balance.py 07_portafolio/
cd 07_portafolio && python3 PF05_balance.py
```

**Mapa de dependencias.**

**Programa [`PF06_dependencias.py`](RECURSOS-TALLER/PF06_dependencias.py).** Lee `PF01_portafolio_candidatos.csv`; las dependencias se escriben dentro del programa. Produce el orden topológico en pantalla y `graficos/PF_dependencias.png`. Se copia a `07_portafolio/` del repositorio del equipo y **se edita con los datos de su organización**: el programa hace el cálculo, las cifras y su justificación son del equipo.

```bash
# desde la raíz del repositorio del equipo; <curso> es la carpeta del material del curso
cp <curso>/SEMANA-13/RECURSOS-TALLER/PF06_dependencias.py 07_portafolio/
cd 07_portafolio && python3 PF06_dependencias.py
```

> **Los proyectos habilitadores** —los que otros necesitan— tienen **prioridad estructural** con independencia de su beneficio propio. La capa de integración y el gobierno del dato rara vez tienen retorno directo, y sin ellos la mitad del portafolio no puede ejecutarse.

### Paso E — Redactar Sección 7.1

```markdown
## 7.1 Portafolio de proyectos

### 7.1.1 Fuentes admisibles y control de admisión
Las cinco fuentes. Candidatos retirados y la razón de su retiro.

### 7.1.2 Portafolio de proyectos
Tabla de los N proyectos con fuente, sección de origen, objetivo y categoría.

### 7.1.3 Fichas de proyecto
Una ficha por proyecto, con los 20 campos.

### 7.1.4 Costo total de propiedad
Tabla de TCO a 5 años, con el **factor TCO/inversión inicial** y su interpretación.
Proyectos de mayor carga operativa recurrente.

### 7.1.5 Casos de negocio de los proyectos de mayor inversión
Tres casos completos, con alternativas, **costo de la inacción** y recomendación.

### 7.1.6 Balance del portafolio
Distribución operar/crecer/transformar, contraste con las proporciones de referencia
y **con el balance actual del presupuesto de la organización (Sección 3.1)**.

### 7.1.7 Dependencias entre proyectos
Mapa de dependencias, orden topológico y proyectos habilitadores.
**Esta secuencia condiciona la hoja de ruta (Sección 7.3).**

### 7.1.8 Cobertura de objetivos
Verificación de que todo objetivo de la sección 6.2 tiene al menos un proyecto asociado.
```

### Paso F — Validar y corregir

El resultado no vale por estar hecho, sino por resistir una comprobación. Se ejecutan estas tres y **se corrige lo que falle antes de cerrar la sesión**.

1. Comprobar que cada proyecto del portafolio cita el objetivo al que responde.
2. Verificar que los duplicados fusionados no perdieron alcance por el camino.
3. Comprobar que el TCO a cinco años incluye el costo operativo, no solo la inversión.

> Lo que no se pueda corregir hoy se anota en la sección **Problemas y mejoras** de la evidencia, con lo que faltó y por qué. Un resultado parcial documentado con honestidad vale más que uno declarado sin prueba.

### Paso G — Registrar la evidencia y cerrar

Se versiona lo producido, se anota la URL de cada resultado y se responde en dos frases la pregunta de transferencia — **qué riesgo correría una organización real si esto se hiciera mal**.

```bash
git add . && git commit -m "S13: portafolio de proyectos, TCO, casos de negocio y dependencias — seccion 7.1"
git tag -a v0.13 -m "PETI v0.13 — portafolio de proyectos"
```

---

## 3. Resultados

> **Evidencia obligatoria en GitHub.** Todo resultado de este taller se versiona en el repositorio del equipo. El informe **no consigna capturas sueltas**. Consigna la **URL** del artefacto en GitHub. Una captura no permite verificar autoría, fecha ni contenido; un enlace sí.
>
> | Qué se entrega | Dónde vive | Qué se escribe en el informe |
> |---|---|---|
> | Programas y archivos CSV del taller | La carpeta de la sección del PETI que el taller indica (esta semana, `07_portafolio/`), en la rama del taller fusionada a `develop` vía Pull Request | URL del Pull Request |
> | Documentos y matrices | La misma carpeta de la sección, en formato de texto versionable | URL del archivo en la rama |
> | Capturas y videos que el taller exija | `evidencias/S13/` | URL del archivo |
> | Salida de comandos | `evidencias/S13/salidas/*.txt` | URL del archivo |
>
> **Etiqueta del taller.** Al cerrar el taller se crea la etiqueta `taller-13` sobre el commit entregado:
>
> ```bash
> git tag -a taller-13 -m "Taller 13 · SI886"
> git push origin taller-13
> ```
>
> La URL que se consigna en el informe apunta a esa etiqueta:
> `https://github.com/<organizacion>/<repositorio>/tree/taller-13`
>
> Esta etiqueta convive con la de versión del PETI que crea el último paso del procedimiento (`v0.13`): `taller-13` marca el commit que se entrega a calificar y `v0.13` marca el estado del documento. Pueden apuntar al mismo commit.
>
> **El informe es lo que se califica; el repositorio es lo que lo prueba.** Cada resultado de la sección 3 del informe lleva la URL con la que se verifica, y **un resultado sin su URL se califica como no logrado**, por bien redactado que esté. Lo que no se puede abrir no se puede dar por hecho.

### 3.1. Los tres resultados que se califican

Son los que la rúbrica evalúa. El resto de la lista tiene que existir, pero no se califica fila por fila.

| Resultado | Qué demuestra | Dónde está |
|---|---|---|
| **El portafolio depurado** | Cada proyecto trazable a un objetivo, sin duplicados | Sección 7.1 |
| **Las fichas de proyecto** | Estandarizadas, con alcance, plazo y orden de magnitud | Fichas |
| **El caso de negocio** | Con las tres alternativas, el TCO a cinco años y el costo de no actuar | `PF04_alternativas.csv` y sección 7.1.5 |

### 3.2. Lista de comprobación del taller

Todo esto debe existir al cerrar la sesión.

| # | Resultado esperado | Verificación |
|---|---|---|
| 1 | Candidatos consolidados desde las **cinco fuentes admisibles** | `PF01_portafolio_candidatos.csv` |
| 2 | **Control de admisión ejecutado**. Candidatos sin fuente o sin objetivo retirados | Salida de `PF01_consolidacion.py` |
| 3 | Portafolio con **≥ 12 proyectos**, cada uno con su sección de origen citada | Misma tabla |
| 4 | Ficha estandarizada de cada proyecto con los **20 campos** | `PF03_fichas/` |
| 5 | **TCO a 5 años** calculado para cada proyecto, con su margen de incertidumbre | `PF02_tco.csv` |
| 6 | **Factor TCO/inversión inicial** calculado e interpretado | Salida de `PF02_tco.py` |
| 7 | Tres casos de negocio con **las tres alternativas**, incluida «no hacer nada» | `PF04_alternativas.csv` |
| 8 | **Costo de la inacción cuantificado** en cada caso de negocio | Misma tabla |
| 9 | Balance operar/crecer/transformar calculado y **contrastado con el balance actual** | Salida de `PF05_balance.py` |
| 10 | Gráficos de balance y de TCO por proyecto | `PF_balance.png` |
| 11 | Mapa de dependencias con **orden topológico** y proyectos habilitadores | `PF_dependencias.png` |
| 12 | **Cobertura verificada**: todo objetivo de la sección 6.2 con al menos un proyecto | Salida del script |
| 13 | Sección 7.1 redactada · etiqueta `v0.13` | `git tag` |

## Rúbrica procedimental (20 puntos)

Se aplica sobre el informe entregado y la evidencia enlazada en el repositorio. **Cada criterio se califica de forma independiente.**

| Criterio | 4 — Logrado | 2 — En proceso | 0 — Insuficiente |
|---|---|---|---|
| **El criterio de éxito** | Se cumple tal como lo pide el reto de esta sesión | Se cumple con reservas que el equipo declara | No se cumple, o se afirma cumplido sin prueba |
| **El portafolio depurado** | Completo y correcto, con la evidencia que lo respalda | Completo con errores menores, o correcto sin toda la evidencia | Incompleto o sin evidencia |
| **Las fichas de proyecto** | Completo y correcto, con la evidencia que lo respalda | Completo con errores menores, o correcto sin toda la evidencia | Incompleto o sin evidencia |
| **El caso de negocio** | Completo y correcto, con la evidencia que lo respalda | Completo con errores menores, o correcto sin toda la evidencia | Incompleto o sin evidencia |
| **La validación** | Las tres comprobaciones ejecutadas, y lo que falló quedó corregido o documentado | Ejecutadas sin corregir lo que falló | No se validó nada |

## 4. Conclusiones

1. El costo total de propiedad suele ser varias veces la inversión inicial; presentar solo esta última ante la gerencia compromete a la organización con un gasto recurrente que nunca aprobó explícitamente.
2. La alternativa «no hacer nada» con su costo cuantificado es la sección más persuasiva del caso de negocio y la que la mayoría de los planes omite, precisamente porque obliga a medir lo que hoy se pierde.
3. Los proyectos habilitadores —integración, gobierno del dato— rara vez tienen retorno propio y sostienen la mitad del portafolio; priorizarlos solo por su beneficio directo bloquea todo lo demás.

## 5. Referencias Bibliográficas

- Project Management Institute. *A Guide to the Project Management Body of Knowledge (PMBOK Guide)*. https://www.pmi.org/
- Project Management Institute. *The Standard for Portfolio Management*. https://www.pmi.org/
- ISO 21500:2021. *Project, programme and portfolio management — Context and concepts*. https://www.iso.org/standard/75704.html
- ISACA. *Val IT Framework — Enterprise Value: Governance of IT Investments*. https://www.isaca.org/resources/frameworks-standards-and-models
- ISACA. (2018). *COBIT 2019*, objetivos **APO05 Managed Portfolio** y **EDM02 Ensured Benefits Delivery**. https://www.isaca.org/resources/cobit
- Rodríguez Bermúdez, J. R. (2015). *Planificación y dirección estratégica de sistemas de información*. Editorial UOC. https://elibro.net/es/lc/bibliotecaupt/titulos/57875
- Resolución de Secretaría de Gobierno Digital 005-2018-PCM/SEGDI, Anexo I — portafolio de proyectos del PGD (Plan de Gobierno Digital). https://cdn.www.gob.pe/uploads/document/file/356863/Anexo_I_Lineamientos_PGD.pdf
- MINTIC Colombia. *Guía para la construcción del PETI* — catálogo de proyectos. https://www.mintic.gov.co/arquitecturati/630/w3-propertyvalue-8114.html

## 6. Anexos

- `anexo_A_portafolio.xlsx`
- `anexo_B_fichas_proyecto.pdf`
- `anexo_C_tco.xlsx`
- `anexo_D_casos_negocio.pdf`
- `anexo_E_balance_portafolio.png`
- `anexo_F_mapa_dependencias.png`

---

---

[Semana 13](README.md) · [Teoría](1-TEORIA.md) · [Dinámica de aula](2-DINAMICA.md) · **Taller de laboratorio**

---

**Docente** · Dr. Oscar Juan Jimenez Flores
[oscarjimenezflores@upt.pe](mailto:oscarjimenezflores@upt.pe) · [LinkedIn](https://www.linkedin.com/in/oscar-jimenez-flores/) · [CTI Vitae — CONCYTEC](https://ctivitae.concytec.gob.pe/appDirectorioCTI/VerDatosInvestigador.do?id_investigador=33398)

Escuela Profesional de Ingeniería de Sistemas · Universidad Privada de Tacna · Tacna, Perú
