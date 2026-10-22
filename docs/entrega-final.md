# Entrega final del proyecto SENA

## Proyecto
Clasificador de mensajes de commit con IA local mediante FastAPI, Ollama y PostgreSQL.

Repositorio: https://github.com/juanjoserodriguezjara0-star/clasificador-commits-ia

## Componentes disponibles en el repositorio
- API REST en `main.py`.
- Validación de entradas y manejo de errores.
- Esquema de base de datos en `db/init.sql`.
- Servicios de API y PostgreSQL definidos en `docker-compose.yml`.
- Imagen de la API definida en `Dockerfile`.
- Pruebas automatizadas en `test_main.py`.
- Flujo de integración continua en `.github/workflows/tests.yml`.
- Prueba de humo k6 en `tests/load.js`.
- Manual técnico, informe técnico y procedimiento de respaldo.

## Evidencia verificable desde GitHub
Las ejecuciones del flujo de GitHub Actions pueden consultarse en:
https://github.com/juanjoserodriguezjara0-star/clasificador-commits-ia/actions

Una ejecución exitosa confirma únicamente los pasos que muestra ese flujo (instalación de dependencias, sintaxis, configuración/build de Docker y pruebas automatizadas). Las pruebas unitarias simulan dependencias externas cuando así se indica en el código.

## Resultados que no deben darse por ejecutados sin evidencia
Los siguientes puntos requieren ejecución real y registro de sus resultados:
- Arranque conjunto de API, Ollama y PostgreSQL.
- Clasificación con el modelo instalado y persistencia de registros reales.
- Ejecución del script k6 y conservación de sus métricas.
- Creación de un respaldo y restauración comprobada en una base temporal.
- Revisión del repositorio por un compañero y evidencia de dicha revisión.
- Publicación de la versión `v1.0.0` después de completar las validaciones.

## Lista de entrega
- [x] Código de la API y validación de mensajes.
- [x] Esquema SQL y configuración de Docker Compose.
- [x] Pruebas automatizadas y flujo de GitHub Actions.
- [x] Manual técnico e informe técnico inicial.
- [x] Plan de validación y procedimiento de respaldo.
- [ ] Evidencia de integración real de los tres servicios.
- [ ] Resultados medidos de la prueba de carga.
- [ ] Evidencia de respaldo y restauración.
- [ ] Revisión auténtica por un compañero, si la guía la exige.
- [ ] Release `v1.0.0` tras completar las validaciones.
- [ ] Entregas en Google Classroom: reflexión, cuestionario, diagnóstico del equipo y publicaciones solicitadas.

## Reflexión sobre IA local (borrador para revisar y publicar)
Una organización puede ejecutar modelos de inteligencia artificial de forma local para tener mayor control sobre sus datos y reducir la dependencia de servicios externos. Esto puede ser importante cuando se procesan datos internos, información de clientes o documentos que no deberían enviarse a plataformas de terceros. También permite trabajar sin conexión estable a Internet y controlar la versión del modelo utilizado. Sin embargo, la ejecución local requiere equipos con recursos suficientes, mantenimiento, actualizaciones y medidas de seguridad. Además, un modelo local puede tener menor capacidad que algunos servicios comerciales y sus resultados deben evaluarse. Por eso, la decisión depende del tipo de información, el presupuesto, la infraestructura y los requisitos de privacidad de la organización.

> Antes de publicar la reflexión en Classroom, personalízala con tu opinión y revisa el límite de palabras indicado por la guía.

## Diagnóstico del computador
No se completan especificaciones de hardware sin medirlas en el equipo real. Registra Windows (`winver`), memoria RAM, espacio libre, tipo de disco y estado de virtualización con los datos reales de tu computador.
