"""
generar_fichas.py
Generador de las 12 Fichas Estandarizadas de Proyecto (20 Campos)
EPS AGUAS DEL SUR S.A. - PETI 2026-2030 (Semana 13)
"""

import os

fichas_datos = [
    {
        "id": "PR-01",
        "nombre": "Sistema Integrado de Gestión Comercial y Facturación Electrónica (SIGECO-Agua)",
        "fuente": "Arquitectura de Aplicaciones",
        "seccion_origen": "Sección 4.3.5",
        "objetivo": "OE-02: Incrementar la recaudación y reducir pérdidas comerciales (agua no facturada) mejorando canales digitales y medición.",
        "categoria": "Transformar",
        "justificacion": "El sistema comercial actual en tecnología cliente-servidor obsoleta presenta caídas frecuentes, desfase de 12 días en emisión de recibos, inconsistencias en lecturas de micromedición y riesgo tributario ante SUNAT por demoras en facturación electrónica masiva.",
        "descripcion": "Implementación de una plataforma web y móvil cloud-native para la gestión integral del ciclo comercial del servicio de saneamiento: catastro de usuarios, micromedición digital en campo, liquidación tarifaria SUNASS, facturación electrónica integrada a OSE/SUNAT, cobranzas y gestión de convenios de pago.",
        "entregables": "1. Módulo de Catastro Comercial y Suministros.\n2. App Móvil de Toma de Lecturas con GPS y captura fotográfica del medidor.\n3. Motor de Facturación y Emisión Electrónica SUNAT.\n4. Módulo de Recaudación, Convenios y Cortes/Reconexiones.\n5. Pasarela de Integración de Pagos Bancarios.",
        "sponsor": "Gerencia Comercial / Jefe de Tecnología de Información",
        "beneficiarios": "Área Comercial, Facturación, Recaudación, 85,000 usuarios conectados del servicio de agua potable.",
        "plazo": "10 meses (Fase 1: Catastro y Lecturas en mes 4; Fase 2: Facturación en mes 7; Fase 3: Recaudación en mes 10).",
        "capex": "S/ 380,000.00 (Margen de incertidumbre: ±15%)",
        "opex": "S/ 65,000.00 anuales (Soporte N2/N3 especializado, actualizaciones regulatorias SUNAT/SUNASS y hosting transaccional).",
        "tco": "S/ 705,000.00 a 5 años | Factor TCO/Inversión: 1.86x",
        "beneficios": "Cuantitativos: Incremento de efectividad de cobranza del 84% al 96%; reducción de cartera morosa en S/ 450,000 anuales; reducción de reclamos por error de lectura en 70%.\nCualitativos: Información comercial en línea, transparencia en cobros y cumplimiento de metas de gestión SUNASS.",
        "riesgos": "Riesgo: Resistencia de lectores de medidores al cambio digital. Mitigación: Talleres participativos de usabilidad e incentivos por precisión de lectura.\nRiesgo: Errores en migración de base de datos histórica. Mitigación: Pruebas paralelas de facturación durante 2 ciclos consecutivos.",
        "dependencias": "PR-06 (Bus de Integración ESB), PR-07 (Repositorio Maestro MDM y BI), PR-03 (Nube Híbrida y DRP).",
        "sostenibilidad": "Economía: Reducción de costos de papel térmico y cobranza física.\nSociedad: Facturación justa basada en consumo real y no promediado.\nMarco Legal: Cumplimiento de R.C.D. SUNASS y normativa de comprobantes electrónicos SUNAT.",
        "kpi": "Efectividad de Cobranza Mensual (%) = (Monto Recaudado / Monto Facturado) * 100 [Meta: >= 95%]. Tiempo de ciclo de facturación [Meta: <= 3 días]."
    },
    {
        "id": "PR-02",
        "nombre": "Plataforma SCADA e Infraestructura IoT de Telemetría de Redes Hidráulicas",
        "fuente": "Arquitectura Tecnológica e Infraestructura",
        "seccion_origen": "Sección 5.4.2",
        "objetivo": "OE-01: Optimizar la continuidad y calidad del suministro de agua potable mediante telemetría y automatización operativa.",
        "categoria": "Transformar",
        "justificacion": "La operación de reservorios y macrosectores de distribución depende de rondas físicas presenciales de operadores. Las roturas de tuberías matrices tardan hasta 6 horas en ser detectadas, provocando pérdidas de agua del 38% e inundaciones urbanas con quejas masivas.",
        "descripcion": "Despliegue de red IoT industrial con sensores de nivel hidrostático, presión en tuberías matrices y caudalímetros electromagnéticos en 8 reservorios y 12 sectores hidráulicos, interconectados mediante protocolos MQTT y LoRaWAN a una plataforma SCADA centralizada con visualización HMI web y alarmas predictivas.",
        "entregables": "1. 35 Nodos de Instrumentación y Sensores IoT (Nivel, Presión, Caudal).\n2. 8 Gabinetes de Telemetría RTU con respaldo solar en reservorios periféricos.\n3. Plataforma SCADA Central (Ignition/SCADA-LTS) con centro de control HMI.\n4. Sistema de Detección Automática de Fugas y Desbalance Hidráulico.\n5. Integración de alertas móviles para cuadrillas de emergencia.",
        "sponsor": "Gerencia de Operaciones e Ingeniería / Jefe de Producción y Mantenimiento",
        "beneficiarios": "Departamento de Operaciones, Cuadrillas de Distribución, 320,000 habitantes abastecidos.",
        "plazo": "12 meses (Fase 1: Reservorios cabecera en mes 4; Fase 2: Redes de distribución en mes 8; Fase 3: Comisionamiento SCADA en mes 12).",
        "capex": "S/ 420,000.00 (Margen de incertidumbre: ±20%)",
        "opex": "S/ 72,000.00 anuales (Calibración semestral de instrumentación, repuestos de sensores y mantenimiento preventivo de RTUs).",
        "tco": "S/ 780,000.00 a 5 años | Factor TCO/Inversión: 1.86x",
        "beneficios": "Cuantitativos: Reducción del tiempo de detección de roturas matrices de 6 horas a 15 minutos; recuperación de 1.2 millones de m³ de agua no facturada al año; ahorro de S/ 180,000 anuales en energía de bombeo.\nCualitativos: Estabilidad de presiones en red domiciliaria y prevención de daños a pavimentos urbanos.",
        "riesgos": "Riesgo: Vandalismo o robo de sensores en reservorios aislados. Mitigación: Instalación en buzones antivandálicos bajo tierra y alarmas perimétricas de intrusión.\nRiesgo: Pérdida de señal en zonas topográficas ciegas. Mitigación: Topología de malla inalámbrica LoRaWAN redundante.",
        "dependencias": "PR-11 (Red WAN y Enlaces Redundantes para Estaciones Remotas).",
        "sostenibilidad": "Medio Ambiente: Ahorro masivo del recurso hídrico en zona de cabecera de desierto (Tacna).\nSociedad: Mayor continuidad del servicio en horas pico (aumento de 16h a 22h promedio de abastecimiento).\nEconomía: Menor gasto operativo en horas extra y camiones cisterna.",
        "kpi": "Índice de Agua No Facturada Operacional (%) [Meta: Reducción de 38% a 26%]. Tiempo de respuesta ante rotura de matriz [Meta: <= 30 minutos]."
    },
    {
        "id": "PR-03",
        "nombre": "Nube Híbrida, Datacenter de Contingencia y Plan de Recuperación ante Desastres (DRP)",
        "fuente": "Arquitectura Tecnológica e Infraestructura",
        "seccion_origen": "Sección 5.4.2",
        "objetivo": "OE-03: Asegurar la continuidad operativa, ciberseguridad y resiliencia de la infraestructura tecnológica crítica.",
        "categoria": "Crecer",
        "justificacion": "La sede central concentra el 100% de los servidores sin redundancia física ni sitio alterno. En caso de sismo de gran magnitud (zona sísmica sur) o incendio, la empresa quedaría completamente inoperativa por semanas, violando normativas de SUNASS y PCM.",
        "descripcion": "Diseño e implementación de arquitectura de nube híbrida activa-pasiva con replicación continua de máquinas virtuales, base de datos de producción y servicios comerciales hacia nube pública (AWS/Azure) con certificación Tier III, acompañada de un DRP formal con simulacros semestrales.",
        "entregables": "1. Infraestructura hiperconvergente local renovada con almacenamiento SSD NVMe.\n2. Bóveda en nube pública con replicación asíncrona continua.\n3. Plan de Recuperación ante Desastres (DRP) documentado con matrices RPO/RTO.\n4. Orquestador de Failover automatizado ante caída de sede principal.\n5. Informe de simulacro de recuperación en caliente certificado por auditor externo.",
        "sponsor": "Gerencia General / Gerente de Administración y Finanzas / Jefe de TI",
        "beneficiarios": "Todas las unidades orgánicas de la EPS y la totalidad de los usuarios del servicio.",
        "plazo": "8 meses (Fase 1: Dimensionamiento y nube en mes 3; Fase 2: Replicación en mes 5; Fase 3: Pruebas DRP en mes 8).",
        "capex": "S/ 290,000.00 (Margen de incertidumbre: ±15%)",
        "opex": "S/ 75,000.00 anuales (Suscripción IaaS nube híbrida, enlace dedicado de contingencia y auditoría de pruebas DRP).",
        "tco": "S/ 665,000.00 a 5 años | Factor TCO/Inversión: 2.29x",
        "beneficios": "Cuantitativos: Reducción del RPO de 24 horas a 15 minutos; reducción del RTO de 14 días a 2 horas en caso de catástrofe; disponibilidad de sistemas del 99.85%.\nCualitativos: Certeza jurídica y financiera de continuidad del negocio institucional ante desastres.",
        "riesgos": "Riesgo: Sobrecostos ocultos por consumo imprevisto de ancho de banda en nube. Mitigación: Contratos de consumo reservado con topes presupuestarios estrictos.\nRiesgo: Desactualización de procedimientos DRP. Mitigación: Ensayos semestrales obligatorios vinculados a evaluación de desempeño del personal de TI.",
        "dependencias": "PR-12 (Sistema Automatizado de Respaldo Corporativo Inmutable).",
        "sostenibilidad": "Marco Legal: Cumplimiento de Resolución de Secretaría de Gobierno Digital 004-2018-PCM/SEGDI sobre Continuidad Operativa.\nEconomía: Prevención de pérdidas catastróficas estimadas en S/ 1,200,000 ante eventos sísmicos.\nSociedad: Garantía de restablecimiento rápido de sistemas para reparto de agua en emergencias.",
        "kpi": "RPO (Recovery Point Objective) [Meta: <= 15 min]. RTO (Recovery Time Objective) [Meta: <= 2 horas]. Disponibilidad de Plataforma Core [Meta: >= 99.85%]."
    },
    {
        "id": "PR-04",
        "nombre": "Plataforma Omnicanal de Autoservicio y Atención al Usuario Ciudadano (Web/Móvil/WhatsApp)",
        "fuente": "Necesidades Estratégicas y Gobierno Digital",
        "seccion_origen": "Sección 6.1.7",
        "objetivo": "OE-05: Modernizar la experiencia y atención al ciudadano usuario mediante plataformas omnicanal y autoservicio transparente.",
        "categoria": "Crecer",
        "justificacion": "El portal de autoservicio cerrado en 2024 (Expediente 1) fracasó por falta de integración, costando S/ 509K con desviación del +62.5% y beneficios no medidos. Los usuarios sufren largas colas presenciales en sede central para pagar o presentar reclamos.",
        "descripcion": "Desarrollo de una suite omnicanal centrada en el usuario que incluye: portal web responsive, app móvil nativa (Android/iOS) y bot verificado de WhatsApp Business API, permitiendo consultar recibos, pagar en línea mediante código QR/tarjetas, reportar fugas en vía pública con foto geolocalizada y dar seguimiento a reclamos SUNASS.",
        "entregables": "1. Portal Web Ciudadano con autenticación vía DNIe / Clave SOL.\n2. App Móvil 'Aguas del Sur Móvil' para Android e iOS.\n3. Chatbot Asistente Virtual en WhatsApp con IA generativa para preguntas frecuentes.\n4. Módulo de Reporte Ciudadano de Fugas y Roturas con georreferenciación.\n5. Pasarela de Pagos Digitales conectada con Niubiz, Izipay y billeteras Yape/Plin.",
        "sponsor": "Gerencia Comercial / Jefe de Atención al Cliente",
        "beneficiarios": "Usuarios domésticos y comerciales de Tacna, operadores de mesa de partes y cobranzas.",
        "plazo": "7 meses (Fase 1: WhatsApp y Web en mes 4; Fase 2: App móvil y pagos integrados en mes 7).",
        "capex": "S/ 160,000.00 (Margen de incertidumbre: ±15%)",
        "opex": "S/ 42,000.00 anuales (API oficial de WhatsApp Business por conversación, pasarela de cobro digital, hosting y soporte).",
        "tco": "S/ 370,000.00 a 5 años | Factor TCO/Inversión: 2.31x",
        "beneficios": "Cuantitativos: Reducción del 55% de afluencia presencial a ventanillas; canalización del 40% de pagos mensuales vía canales digitales; reducción del costo unitario de cobranza de S/ 3.20 a S/ 0.45 por recibo.\nCualitativos: Satisfacción ciudadana, transparencia en cobros y menor congestión de trámites.",
        "riesgos": "Riesgo: Baja adopción digital en usuarios adultos mayores. Mitigación: Campañas pedagógicas en centros comunales e interfaz amigable de fácil uso por WhatsApp.\nRiesgo: Intentos de fraude en pasarela web. Mitigación: Doble factor de autenticación y cumplimiento de normas PCI-DSS.",
        "dependencias": "PR-06 (Bus de Integración ESB), PR-03 (Nube Híbrida), PR-09 (Ciberseguridad y WAF).",
        "sostenibilidad": "Sociedad: Ahorro de tiempo y pasajes a más de 35,000 familias usuarias al evitar traslados a la oficina.\nEconomía: Descongestión operativa de ventanillas y mayor velocidad en flujo de caja.\nMedio Ambiente: Supresión de 180,000 recibos impresos físicos por año (facturación electrónica ecológica).",
        "kpi": "Porcentaje de recaudación canalizada digitalmente (%) [Meta: >= 35%]. Nivel de satisfacción de atención al usuario (CSAT) [Meta: >= 85%]."
    },
    {
        "id": "PR-05",
        "nombre": "Sistema de Información Geográfica (GIS) Corporativo para Redes de Agua y Alcantarillado",
        "fuente": "Arquitectura de Información y Datos",
        "seccion_origen": "Sección 4.1.5",
        "objetivo": "OE-01: Optimizar la continuidad y calidad del suministro de agua potable mediante telemetría y automatización operativa.",
        "categoria": "Transformar",
        "justificacion": "La información sobre ubicación de tuberías, válvulas de corte y conexiones domiciliarias reside en planos físicos en papel y archivos CAD obsoletos y desarticulados. En emergencias, las cuadrillas tardan hasta 3 horas en ubicar la válvula correcta para aislar un sector.",
        "descripcion": "Construcción de un geoportal corporativo (QGIS Server / PostGIS) con cartografía georreferenciada de las redes de distribución de agua potable y alcantarillado, integrando el catastro comercial de usuarios, modelo hidráulico de presiones y capas de telemetría en tiempo real.",
        "entregables": "1. Base de Datos Geográfica Espacial Normalizada (PostGIS).\n2. Geoportal Web Institucional de Redes de Agua y Alcantarillado.\n3. Aplicativo GIS Móvil para cuadrillas operativas en campo con modo desconectado.\n4. Integración del Catastro Comercial con conexiones domiciliarias geolocalizadas.\n5. Capa de zonificación por sectores hidráulicos y ubicación de válvulas de aislamiento.",
        "sponsor": "Gerencia de Operaciones / Jefe de Estudios y Proyectos",
        "beneficiarios": "Cuadrillas operativas de distribución, ingeniería, planificación de inversiones, área comercial.",
        "plazo": "11 meses (Fase 1: Modelo de datos y migración CAD en mes 4; Fase 2: Geoportal en mes 7; Fase 3: App móvil cuadrillas en mes 11).",
        "capex": "S/ 240,000.00 (Margen de incertidumbre: ±20%)",
        "opex": "S/ 48,000.00 anuales (Mantenimiento de servidor de mapas, actualización de ortofotos satelitales y soporte SIG).",
        "tco": "S/ 480,000.00 a 5 años | Factor TCO/Inversión: 2.00x",
        "beneficios": "Cuantitativos: Reducción del tiempo de aislamiento de sectores ante roturas de 180 min a 20 min; disminución de roturas involuntarias por terceros en obras municipales en 60%.\nCualitativos: Visibilidad completa del activo enterrado y sustento técnico de planes de reposición de redes para SUNASS.",
        "riesgos": "Riesgo: Imprecisiones en planos históricos heredados. Mitigación: Campaña de validación en campo mediante georadar y GPS submétrico en obras en curso.\nRiesgo: Falta de actualización continua por cuadrillas. Mitigación: Cierre de órdenes de trabajo condicionado a registro fotográfico y coordenadas georreferenciadas.",
        "dependencias": "PR-06 (Bus ESB), PR-07 (MDM y Datos Maestros), PR-02 (SCADA e IoT).",
        "sostenibilidad": "Medio Ambiente: Disminución de aniegos de aguas residuales y pérdidas de agua potable por rápida maniobra de válvulas.\nEconomía: Optimización del gasto en reposición de tuberías por conocimiento exacto de antigüedad y material.\nSociedad: Menor interrupción vial por roturas descontroladas.",
        "kpi": "Porcentaje de red de agua y alcantarillado digitalizada en GIS [Meta: 100% casco urbano]. Tiempo de maniobra de corte de sector [Meta: <= 20 min]."
    },
    {
        "id": "PR-06",
        "nombre": "Bus de Integración de Servicios (ESB / API Gateway) e Interoperabilidad",
        "fuente": "Arquitectura de Aplicaciones",
        "seccion_origen": "Sección 4.3.5",
        "objetivo": "OE-04: Fortalecer la gobernanza de datos y la interoperabilidad institucional cumpliendo normativas de SUNASS y Gobierno Digital.",
        "categoria": "Crecer",
        "justificacion": "Las aplicaciones existentes funcionan como silos aislados mediante conexiones punto a punto frágiles o exportaciones manuales de archivos Excel. No existe una capa formal de integración segura ni conexión con la Plataforma Nacional de Interoperabilidad (PIDE).",
        "descripcion": "Implementación de una plataforma de middleware orientada a servicios (SOA / Microservicios) y API Gateway (Kong / Apache WSO2) para orquestar los flujos de información entre ERP, SIGECO, GIS, SCADA y entidades gubernamentales como SUNASS, RENIEC y SUNAT.",
        "entregables": "1. Plataforma de API Gateway y Service Bus instalada en alta disponibilidad.\n2. Catálogo de APIs RESTful y servicios SOAP institucionales estandarizados.\n3. Conector de interoperabilidad con la Plataforma Nacional de Interoperabilidad (PIDE).\n4. Módulo de seguridad, control de cuotas, throttling y autenticación JWT/OAuth2.\n5. Tablero de monitoreo y trazabilidad transaccional en tiempo real.",
        "sponsor": "Gerencia de Administración y Finanzas / Jefe de Tecnología de Información",
        "beneficiarios": "Área de TI, todas las áreas de negocio, SUNASS, entidades financieras y plataformas ciudadanas.",
        "plazo": "6 meses (Fase 1: Arquitectura y core en mes 2; Fase 2: APIs comerciales y operacionales en mes 4; Fase 3: Conexión PIDE/SUNASS en mes 6).",
        "capex": "S/ 150,000.00 (Margen de incertidumbre: ±15%)",
        "opex": "S/ 35,000.00 anuales (Soporte enterprise, monitoreo de microservicios y gestión de certificados digitales SSL/TLS).",
        "tco": "S/ 325,000.00 a 5 años | Factor TCO/Inversión: 2.17x",
        "beneficios": "Cuantitativos: Reducción del 80% en tiempo y costo de desarrollo de nuevas integraciones; eliminación de errores de doble digitación manual en un 100%; latencia de intercambio de datos < 200 ms.\nCualitativos: Habilitador estructural del portafolio; desacoplamiento de sistemas y cumplimiento de estándares de gobierno digital.",
        "riesgos": "Riesgo: El bus se convierta en cuello de botella o punto único de falla. Mitigación: Despliegue en clúster balanceado activo-activo con escalamiento automático.\nRiesgo: Vulnerabilidades de seguridad en APIs expuestas. Mitigación: Inspección de tráfico mediante WAF y auditoría continua de endpoints.",
        "dependencias": "Ninguno (Proyecto Habilitador Base de Nivel 1).",
        "sostenibilidad": "Marco Legal: Cumplimiento de la Ley de Gobierno Digital (D.L. 1412) y normativa de interoperabilidad del Estado peruano.\nSociedad: Validación instantánea de identidad ciudadana con RENIEC sin exigir copia de DNI.\nEconomía: Ahorro masivo en consultorías de integración punto a punto.",
        "kpi": "Número de APIs operativas catalogadas [Meta: >= 15 APIs]. Disponibilidad del bus transaccional [Meta: >= 99.9%]."
    },
    {
        "id": "PR-07",
        "nombre": "Repositorio Maestro de Datos (MDM), Gobierno del Dato y Plataforma de Analítica (BI)",
        "fuente": "Arquitectura de Información y Datos",
        "seccion_origen": "Sección 4.1.5",
        "objetivo": "OE-04: Fortalecer la gobernanza de datos y la interoperabilidad institucional cumpliendo normativas de SUNASS y Gobierno Digital.",
        "categoria": "Crecer",
        "justificacion": "Existen discrepancias severas entre los registros de usuarios del sistema comercial, la base de datos de micromedición y el catastro técnico. La gerencia no dispone de reportes confiables en tiempo real sobre recaudación, pérdidas de agua ni rendimiento operativo.",
        "descripcion": "Establecimiento del marco de gobierno de datos institucional (DAMA-DMBOK), unificación del modelo maestro de entidades (Cliente, Suministro, Predio, Activo) e implementación de un Data Warehouse corporativo con dashboards analíticos gerenciales en PowerBI/Superset.",
        "entregables": "1. Diccionario de Datos y Catálogo de Gobernanza Institucional.\n2. Repositorio Maestro de Datos (MDM) de Usuarios y Suministros.\n3. Pipelines automatizados de Extracción, Transformación y Carga (ETL).\n4. Data Marts Analíticos (Comercial, Operaciones, Financiero, Recursos Humanos).\n5. Cuadros de Mando Integrales (Dashboards) para Directorio y Gerencia General.",
        "sponsor": "Gerencia General / Gerente de Planificación y Presupuesto",
        "beneficiarios": "Directorio, Gerencia General, Gerencia Comercial, Operaciones, SUNASS.",
        "plazo": "8 meses (Fase 1: Gobierno y catálogo en mes 3; Fase 2: MDM y ETL en mes 5; Fase 3: Dashboards gerenciales en mes 8).",
        "capex": "S/ 180,000.00 (Margen de incertidumbre: ±15%)",
        "opex": "S/ 38,000.00 anuales (Suscripciones de visualización analítica, mantenimiento y optimización de pipelines ETL y auditoría de calidad).",
        "tco": "S/ 370,000.00 a 5 años | Factor TCO/Inversión: 2.06x",
        "beneficios": "Cuantitativos: Reducción del tiempo de elaboración de reportes regulatorios para SUNASS de 15 días a 1 hora; eliminación de discrepancias de datos interdepartamentales del 22% a 0%; toma de decisiones basada en datos.\nCualitativos: Transparencia institucional, confiabilidad en la información estratégica y cultura orientada al dato.",
        "riesgos": "Riesgo: Mala calidad de datos heredados ('basura entra, basura sale'). Mitigación: Fase intensiva previa de limpieza, deduplicación y reglas de validación en origen.\nRiesgo: Falta de adopción de tableros por gerentes acostumbrados al papel. Mitigación: Talleres de capacitación ejecutiva en data literacy.",
        "dependencias": "Ninguno (Proyecto Habilitador Base de Nivel 1).",
        "sostenibilidad": "Economía: Identificación rápida de desvíos presupuestales y morosidad atípica.\nSociedad: Publicación de datos abiertos sobre calidad del servicio en el Portal de Transparencia Estándar.\nMarco Legal: Cumplimiento de directivas de Secretaría de Gobierno y Transformación Digital (SGTD).",
        "kpi": "Índice de consistencia del dato maestro (%) [Meta: >= 98%]. Tiempo de generación de reportes mensuales SUNASS [Meta: <= 2 horas]."
    },
    {
        "id": "PR-08",
        "nombre": "Sistema de Gestión de Mantenimiento de Activos Electromecánicos y Redes (CMMS / GMAO)",
        "fuente": "Diagnóstico y Madurez de TI",
        "seccion_origen": "Sección 3.5",
        "objetivo": "OE-01: Optimizar la continuidad y calidad del suministro de agua potable mediante telemetría y automatización operativa.",
        "categoria": "Operar",
        "justificacion": "El mantenimiento de estaciones de bombeo, pozos y plantas de tratamiento se ejecuta de forma netamente reactiva cuando los equipos ya sufrieron averías graves. No existen hojas de vida digitales de activos ni control de repuestos en almacén.",
        "descripcion": "Implementación de un sistema CMMS/GMAO para la gestión integral del ciclo de vida de los activos electromecánicos e hidráulicos de la empresa, programando mantenimientos preventivos y predictivos por horómetro y emitiendo órdenes de trabajo digitales a cuadrillas móviles.",
        "entregables": "1. Catálogo estructurado de activos con jerarquía técnica e identificación QR.\n2. Módulo de Planificación de Mantenimiento Preventivo y Rutinas de Inspección.\n3. App Móvil de Órdenes de Trabajo (OT) con firma digital y fotos de avance.\n4. Módulo de Gestión de Inventario de Repuestos Críticos y Costos de Mantenimiento.\n5. Indicadores técnicos de confiabilidad y disponibilidad de activos (MTBF, MTTR).",
        "sponsor": "Gerencia de Operaciones / Jefe de Mantenimiento Electromecánico",
        "beneficiarios": "Departamento de Mantenimiento, Cuadrillas de Redes, Almacén de Repuestos.",
        "plazo": "6 meses (Fase 1: Catastro de activos en mes 2; Fase 2: Configuración preventiva en mes 4; Fase 3: App móvil en mes 6).",
        "capex": "S/ 140,000.00 (Margen de incertidumbre: ±15%)",
        "opex": "S/ 32,000.00 anuales (Licenciamiento de cuadrillas, soporte técnico y actualización de librerías de componentes).",
        "tco": "S/ 300,000.00 a 5 años | Factor TCO/Inversión: 2.14x",
        "beneficios": "Cuantitativos: Reducción del 45% en paradas intempestivas de equipos de bombeo; extensión de vida útil de motores y bombas en 3.5 años; ahorro de S/ 110,000 anuales en compras de emergencia de repuestos.\nCualitativos: Trazabilidad total de intervenciones, seguridad ocupacional y orden operacional.",
        "riesgos": "Riesgo: Resistencia de técnicos mecánicos a registrar datos en tablets. Mitigación: Simplificación extrema de pantallas táctiles y capacitación en talleres de campo.\nRiesgo: Falta de stock de repuestos para mantenimientos programados. Mitigación: Integración con módulo de compras para reorden automático por stock mínimo.",
        "dependencias": "PR-02 (Plataforma SCADA e IoT de Telemetría).",
        "sostenibilidad": "Economía: Reducción drástica del costo de reparaciones mayores no programadas.\nSalud y Seguridad: Prevención de accidentes laborales mediante checklists de seguridad en la orden de trabajo digital.\nMedio Ambiente: Mayor eficiencia energética en motores y prevención de derrames de aceites lubricantes.",
        "kpi": "Cumplimiento del Plan de Mantenimiento Preventivo (%) [Meta: >= 90%]. MTTR (Mean Time to Repair) [Meta: Reducción del 40%]."
    },
    {
        "id": "PR-09",
        "nombre": "Fortalecimiento de la Ciberseguridad de Redes OT/IT y Centro de Operaciones de Seguridad (SOC)",
        "fuente": "Arquitectura Tecnológica e Infraestructura",
        "seccion_origen": "Sección 5.4.2",
        "objetivo": "OE-03: Asegurar la continuidad operativa, ciberseguridad y resiliencia de la infraestructura tecnológica crítica.",
        "categoria": "Operar",
        "justificacion": "Las redes de control industrial SCADA y las redes administrativas de oficina se encuentran deficientemente segmentadas. Los equipos carecen de monitoreo proactivo contra malware y no existe un protocolo formal de respuesta a incidentes cibernéticos en infraestructura crítica de saneamiento.",
        "descripcion": "Despliegue de controles avanzados de seguridad de la información: segmentación estricta entre redes corporativas y redes industriales de plantas (norma ISA/IEC 62443), protección en endpoints con EDR centralizado, firewalls de próxima generación (NGFW) y contratación de servicio administrado SOC 24/7.",
        "entregables": "1. Firewalls de Siguiente Generación (NGFW) con segmentación VLAN OT/IT.\n2. Plataforma EDR (Endpoint Detection and Response) para servidores y estaciones.\n3. Servicio Gestionado SOC (Security Operations Center) 24/7/365.\n4. Políticas de Seguridad de la Información (SGSI) alineadas a NTP-ISO/IEC 27001.\n5. Plan de Respuesta ante Incidentes de Ciberseguridad y campañas de concientización.",
        "sponsor": "Gerencia General / Oficial de Seguridad de la Información (CISO) / Jefe de TI",
        "beneficiarios": "Toda la organización, usuarios del servicio y sistemas de control industrial.",
        "plazo": "7 meses (Fase 1: Segmentación y firewalls en mes 3; Fase 2: EDR y SOC en mes 5; Fase 3: Concientización y simulacro phishing en mes 7).",
        "capex": "S/ 190,000.00 (Margen de incertidumbre: ±15%)",
        "opex": "S/ 55,000.00 anuales (Suscripción de servicio gestionado SOC 24/7, licenciamiento EDR y feed de inteligencia de amenazas cibernéticas).",
        "tco": "S/ 465,000.00 a 5 años | Factor TCO/Inversión: 2.45x",
        "beneficios": "Cuantitativos: Detección y contención de amenazas en < 15 minutos; 0 incidentes de secuestro de datos (ransomware); cumplimiento al 100% de disposiciones del Centro Nacional de Seguridad Digital (CNSD).\nCualitativos: Blindaje de la infraestructura crítica de potabilización de agua potable contra ataques o sabotaje externo.",
        "riesgos": "Riesgo: Falsos positivos que bloqueen comunicaciones legítimas de SCADA. Mitigación: Periodo de aprendizaje y simulación en modo auditoría durante 30 días antes del bloqueo activo.\nRiesgo: Ataques de phishing exitosos a usuarios distraídos. Mitigación: Simulaciones mensuales de phishing con retroalimentación inmediata.",
        "dependencias": "PR-11 (Red WAN Segura), PR-12 (Respaldo Inmutable Anti-Ransomware).",
        "sostenibilidad": "Marco Legal: Cumplimiento de la Ley Marco de Ciberseguridad del Perú (D.U. 007-2020) y R.S.G.D. 003-2021-PCM/SEGDI.\nSociedad: Protección de la salud pública al evitar alteraciones maliciosas en la dosificación de químicos en plantas.\nEconomía: Prevención de extorsiones por rescate cibernético y multas regulatorias.",
        "kpi": "Tiempo medio de detección de incidentes (MTTD) [Meta: <= 10 min]. Tiempo medio de contención (MTTC) [Meta: <= 30 min]."
    },
    {
        "id": "PR-10",
        "nombre": "Sistema de Monitoreo Automatizado de Calidad de Agua y Alerta Temprana",
        "fuente": "Necesidades Estratégicas y Gobierno Digital",
        "seccion_origen": "Sección 6.1.7",
        "objetivo": "OE-01: Optimizar la continuidad y calidad del suministro de agua potable mediante telemetría y automatización operativa.",
        "categoria": "Crecer",
        "justificacion": "Los análisis de cloro residual libre, turbidez y pH se realizan mediante muestreo manual puntual en frascos, lo que genera retrasos de hasta 24 horas en detectar variaciones en la calidad del agua distribuida a la población, arriesgando sanciones de DIGESA/SUNASS.",
        "descripcion": "Instalación de estaciones compactas de monitoreo continuo en línea con sensores ópticos y electroquímicos para la medición automática de parámetros clave del agua tratada (cloro, turbidez, pH, conductividad) con transmisión en tiempo real y disparo de alarmas ante desviaciones de la norma sanitaria.",
        "entregables": "1. 10 Estaciones de Monitoreo en Línea instaladas en salidas de PTAP y reservorios clave.\n2. Sensores analizadores de cloro residual amperométricos y turbidímetros automáticos.\n3. Panel de Visualización y Registro Histórico de Calidad de Agua.\n4. Sistema de Alerta Temprana SMS/Correo ante eventos anómalos de turbidez.\n5. Módulo de Generación Automática del Reporte de Calidad para SUNASS y DIGESA.",
        "sponsor": "Gerencia de Operaciones / Jefe de Aseguramiento de Calidad y Laboratorio",
        "beneficiarios": "Población abastecida de Tacna, Laboratorio de Calidad, DIGESA, SUNASS.",
        "plazo": "8 meses (Fase 1: Estaciones en plantas en mes 4; Fase 2: Nodos de red en mes 6; Fase 3: Integración y calibración en mes 8).",
        "capex": "S/ 210,000.00 (Margen de incertidumbre: ±20%)",
        "opex": "S/ 45,000.00 anuales (Reactivos químicos patrón, reposición de electrolitos, calibración semestral INACAL y enlace de datos).",
        "tco": "S/ 435,000.00 a 5 años | Factor TCO/Inversión: 2.07x",
        "beneficios": "Cuantitativos: Monitoreo 24/7 los 365 días del año sin interrupción; detección de anomalías en < 5 minutos; 0 eventos de distribución de agua fuera de norma sanitaria.\nCualitativos: Garantía de inocuidad y potabilidad del agua consumida por la población; confianza ciudadana y cumplimiento estricto de estándares sanitarios.",
        "riesgos": "Riesgo: Ensuciamiento rápido de sensores ópticos por lodos o algas. Mitigación: Sensores con sistema de autolimpieza por chorro de aire comprimido ultrasónico.\nRiesgo: Falta de reactivos químicos en el mercado local. Mitigación: Contrato anual de suministro continuo con reposición automática garantizada.",
        "dependencias": "PR-06 (Bus ESB), PR-02 (SCADA e IoT de Telemetría).",
        "sostenibilidad": "Salud y Seguridad: Prevención directa de brotes de enfermedades diarreicas agudas (EDAs) en la población infantil.\nSociedad: Agua 100% segura y apta para consumo humano en toda la red.\nMarco Legal: Cumplimiento obligatorio del Reglamento de Calidad del Agua para Consumo Humano (D.S. 031-2010-SA).",
        "kpi": "Porcentaje de muestras dentro del rango normativo de cloro residual (0.5 a 1.5 mg/L) [Meta: >= 99.5%]. Tiempo de alerta ante turbidez anómala [Meta: <= 5 min]."
    },
    {
        "id": "PR-11",
        "nombre": "Rediseño y Renovación de la Red WAN de Enlaces de Datos Redundantes para Estaciones Remotas",
        "fuente": "Diagnóstico y Madurez de TI",
        "seccion_origen": "Sección 3.5",
        "objetivo": "OE-03: Asegurar la continuidad operativa, ciberseguridad y resiliencia de la infraestructura tecnológica crítica.",
        "categoria": "Operar",
        "justificacion": "El Expediente 3 evidenció que el enlace redundante ejecutado en 2023 sufrió un sobrecosto del +32.9% y no funcionó adecuadamente por falta de diseño integral. Actualmente, las estaciones remotas de bombeo sufren constantes desconexiones por microondas de baja potencia.",
        "descripcion": "Diseño e implementación de una red WAN corporativa robusta y de alta disponibilidad basada en tecnología SD-WAN, combinando enlaces principales de fibra óptica y radioenlaces microondas licenciados con respaldo automático satelital de baja órbita (Starlink) para 14 instalaciones críticas.",
        "entregables": "1. 14 Enrutadores SD-WAN perimetrales con balanceo de carga y failover automático.\n2. Radioenlaces microondas punto a punto renovados en banda licenciada.\n3. 6 Terminales satelitales Starlink para estaciones de captación de cabecera en zonas agrestes.\n4. Conexión de fibra óptica dedicada para plantas de tratamiento principales (Calana y Pocollay).\n5. Plataforma de monitoreo de enlaces WAN con alertas de degradación de jitter y latencia.",
        "sponsor": "Gerencia de Administración y Finanzas / Jefe de Tecnología de Información",
        "beneficiarios": "Operadores de plantas, técnicos de mantenimiento, sistemas SCADA y comerciales.",
        "plazo": "5 meses (Fase 1: Troncal de fibra en mes 2; Fase 2: Microondas y SD-WAN en mes 4; Fase 3: Terminales satelitales en mes 5).",
        "capex": "S/ 130,000.00 (Margen de incertidumbre: ±15%)",
        "opex": "S/ 52,000.00 anuales (Abonos mensuales de enlaces corporativos dedicados y suscripción satelital Starlink).",
        "tco": "S/ 390,000.00 a 5 años | Factor TCO/Inversión: 3.00x",
        "beneficios": "Cuantitativos: Disponibilidad de enlaces WAN incrementada de 91.2% a 99.8%; tiempo de failover automático < 3 segundos; 0 pérdidas de sesión de telemetría.\nCualitativos: Conectividad ininterrumpida que viabiliza el funcionamiento continuo de SCADA, monitoreo de calidad y cámaras de seguridad perimetral.",
        "riesgos": "Riesgo: Caída de enlaces por condiciones climáticas adversas (vientos y neblina densa). Mitigación: Diversidad de medios físicos (fibra terrestre + satélite no afectado por clima local).\nRiesgo: Retrasos en autorizaciones de instalación de torres en terrenos comunales. Mitigación: Uso exclusivo de infraestructura existente de reservorios propios.",
        "dependencias": "Ninguno (Proyecto Habilitador Base de Nivel 1).",
        "sostenibilidad": "Economía: Optimización del costo por megabit mediante enrutamiento inteligente por calidad de servicio (QoS).\nSociedad: Continuidad del servicio de bombeo y distribución sin cortes por incomunicación.\nMarco Legal: Cumplimiento de normas MTC sobre telecomunicaciones y bandas licenciadas.",
        "kpi": "Disponibilidad promedio de la red WAN corporativa (%) [Meta: >= 99.8%]. Tiempo de conmutación ante caída de enlace principal [Meta: <= 3 seg]."
    },
    {
        "id": "PR-12",
        "nombre": "Sistema Automatizado de Respaldo Corporativo Inmutable y Protección contra Ransomware",
        "fuente": "Diagnóstico y Madurez de TI",
        "seccion_origen": "Sección 3.5",
        "objetivo": "OE-03: Asegurar la continuidad operativa, ciberseguridad y resiliencia de la infraestructura tecnológica crítica.",
        "categoria": "Operar",
        "justificacion": "El Expediente 2 (2024) costó S/ 375K con desviación de +34.0%, justificado verbalmente sin caso de negocio ni medición de beneficios. La infraestructura resultante no protege contra ataques sofisticados de ransomware que cifran los propios respaldos.",
        "descripcion": "Modernización de la plataforma de copias de seguridad mediante almacenamiento de escritura única y lectura múltiple (WORM / Air-gapped inmutable), automatizando la regla de respaldo 3-2-1-1-0 con cifrado AES-256 y verificación periódica de integridad de arranque de máquinas virtuales.",
        "entregables": "1. Servidor Appliance de almacenamiento inmutable WORM en sitio físico local.\n2. Software de respaldo corporativo empresarial con protección anti-ransomware (Veeam/Commvault).\n3. Replicación externa hacia bóveda aislada (Air-gapped) en nube con bloqueo de retención inalterable.\n4. Cronograma de pruebas automatizadas de restauración con verificación de arranque (SureBackup).\n5. Procedimiento operativo estandarizado de recuperación rápida ante contingencias.",
        "sponsor": "Gerencia de Administración y Finanzas / Jefe de Tecnología de Información",
        "beneficiarios": "Área de TI, todos los custodios de datos institucionales, gerencias de línea.",
        "plazo": "4 meses (Fase 1: Appliance inmutable en mes 2; Fase 2: Configuración y políticas en mes 3; Fase 3: Pruebas de restauración en mes 4).",
        "capex": "S/ 120,000.00 (Margen de incertidumbre: ±15%)",
        "opex": "S/ 30,000.00 anuales (Mantenimiento de hardware, soporte enterprise de licencias y almacenamiento inmutable en nube).",
        "tco": "S/ 270,000.00 a 5 años | Factor TCO/Inversión: 2.25x",
        "beneficios": "Cuantitativos: Garantía de recuperación del 100% de la información comercial y financiera sin pagar rescate; tiempo de verificación de respaldo reducido de 8 horas a 30 minutos diarios de forma autónoma.\nCualitativos: Eliminación definitiva de la vulnerabilidad señalada en la auditoría del caso del curso y cumplimiento de mejores prácticas ISO 27001.",
        "riesgos": "Riesgo: Espacio insuficiente en el almacenamiento inmutable por retención excesiva. Mitigación: Políticas de deduplicación y compresión de datos con compresión variable.\nRiesgo: Llaves de cifrado extraviadas por rotación de personal. Mitigación: Custodia de claves mediante módulo de seguridad HSM y procedimiento dual de apertura de bóveda.",
        "dependencias": "Ninguno (Proyecto Habilitador Base de Nivel 1).",
        "sostenibilidad": "Economía: Ahorro potencial de cientos de miles de soles ante intentos de extorsión digital.\nMarco Legal: Cumplimiento de la Ley de Protección de Datos Personales (Ley 29733) y normativas de gobierno digital.\nSociedad: Resguardo inviolable de los expedientes históricos de los ciudadanos de Tacna.",
        "kpi": "Tasa de éxito en pruebas automatizadas de restauración (%) [Meta: 100%]. Antigüedad de respaldo verificable [Meta: <= 24 horas]."
    }
]

os.makedirs("07_portafolio/PF03_fichas", exist_ok=True)

for p in fichas_datos:
    md_content = f"""# Ficha Estandarizada de Proyecto: {p['id']}

## 1. Identificación y Alineamiento
* **1. Código del Proyecto:** `{p['id']}`
* **2. Nombre del Proyecto:** {p['nombre']}
* **3. Fuente Admisible:** {p['fuente']}
* **4. Sección de Origen del PETI:** {p['seccion_origen']}
* **5. Objetivo Estratégico al que Responde:** {p['objetivo']}
* **6. Categoría Estratégica:** `{p['categoria']}` (Operar / Crecer / Transformar)

---

## 2. Definición del Alcance y Gobernanza
* **7. Justificación y Caso de Necesidad:**
  {p['justificacion']}
* **8. Descripción y Alcance del Proyecto:**
  {p['descripcion']}
* **9. Entregables Principales:**
```
{p['entregables']}
```
* **10. Sponsor y Líder del Proyecto:** {p['sponsor']}
* **11. Área Usuaria y Beneficiarios:** {p['beneficiarios']}
* **12. Plazo Estimado de Ejecución:** {p['plazo']}

---

## 3. Costo Total de Propiedad (TCO) y Viabilidad Financiera
* **13. Inversión Inicial Estimada (Capex):** {p['capex']}
* **14. Costo Operativo Anual Estimado (Opex):** {p['opex']}
* **15. Costo Total de Propiedad a 5 Años (TCO):** {p['tco']}
* **16. Beneficios Esperados:**
  {p['beneficios']}

---

## 4. Gestión de Riesgos, Dependencias e Impacto
* **17. Riesgos Principales y Plan de Mitigación:**
  {p['riesgos']}
* **18. Proyectos Prerrequisito / Dependencias:** {p['dependencias']}
* **19. Impacto en el Desarrollo Sostenible:**
  {p['sostenibilidad']}
* **20. Indicador de Éxito / Métrica de Valor Entregado (KPI):**
  `{p['kpi']}`
"""
    file_path = f"07_portafolio/PF03_fichas/{p['id']}.md"
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(md_content)

print(f"[OK] Generadas exitosamente las 12 fichas estandarizadas de proyecto en 07_portafolio/PF03_fichas/")
