# Informe técnico

## 1. Objetivo

Implementar una API que clasifique mensajes de commit con un modelo local de lenguaje y registre cada inferencia para su consulta posterior.

## 2. Tecnologías

- Python 3.12
- FastAPI y Pydantic para la API y la validación de entradas
- Ollama con el modelo `qwen2.5-coder:1.5b`
- PostgreSQL para persistencia
- Docker y Docker Compose para ejecución
- pytest y GitHub Actions para pruebas automatizadas
- k6 para pruebas básicas de carga

## 3. Diseño

El cliente envía un mensaje a `POST /clasificar`. FastAPI valida la entrada, envía instrucciones a Ollama, valida la etiqueta devuelta contra las seis categorías permitidas y guarda el resultado en PostgreSQL. Las inferencias se consultan con `GET /inferencias`.

## 4. Categorías

| Categoría | Significado |
|---|---|
| `feat` | Nueva funcionalidad |
| `fix` | Corrección de errores |
| `docs` | Documentación |
| `test` | Pruebas |
| `chore` | Mantenimiento |
| `refactor` | Reorganización interna sin cambiar el comportamiento |

## 5. Validación y pruebas

### 5.1 Pruebas automatizadas

Se ejecutó `pytest -v` y se obtuvieron 10 pruebas aprobadas. Las pruebas comprueban el comportamiento de la API, la validación de entradas y el tratamiento de errores. Las llamadas al modelo se sustituyen por respuestas controladas para evitar depender de la red y del tiempo de inferencia.

### 5.2 Prueba de integración real

Se verificó la API con Ollama y PostgreSQL activos. El endpoint `GET /health` informó que los servicios de API, Ollama y PostgreSQL estaban disponibles.

Se envió a `POST /clasificar` el mensaje `fix: corregir error al iniciar sesión`. La API devolvió la categoría `fix` y un identificador de registro. Después, `GET /inferencias` permitió consultar el registro almacenado.

### 5.3 Prueba de carga con k6

Se ejecutó `k6 run tests/load.js` contra la ruta principal de la API, con un usuario virtual y cinco iteraciones.

| Métrica | Resultado | Criterio configurado | Estado |
|---|---:|---:|---|
| Solicitudes HTTP | 5 | 5 iteraciones | Completado |
| Comprobaciones correctas | 10 de 10 | Todas correctas | Aprobado |
| Solicitudes fallidas | 0 % | Menos del 1 % | Aprobado |
| Duración p95 | 7,35 ms | Menos de 2.000 ms | Aprobado |
| Estado HTTP | 200 | HTTP 200 | Aprobado |
| Campo `version` | Presente | Debe existir | Aprobado |

Estos resultados corresponden a una prueba pequeña de `GET /`. No representan una medición de concurrencia elevada ni del tiempo de inferencia del modelo durante la clasificación.

No se presentan métricas de precisión, exhaustividad o F1 porque todavía no se ha ejecutado una evaluación con un conjunto de mensajes etiquetados.

## 6. Riesgos y limitaciones

- Un modelo pequeño puede clasificar incorrectamente mensajes ambiguos.
- La disponibilidad depende de Ollama y PostgreSQL.
- Las credenciales de ejemplo de Docker Compose son solo para desarrollo.
- Las pruebas unitarias no sustituyen una prueba de integración con los servicios reales.
- La prueba de carga realizada es básica y no permite concluir cómo se comporta el sistema con muchos usuarios simultáneos.

## 7. Mejoras futuras

- Crear un conjunto etiquetado de mensajes y medir precisión, exhaustividad y F1 por categoría.
- Ampliar las pruebas de carga con más usuarios virtuales y solicitudes.
- Añadir autenticación, límites de solicitudes y observabilidad.
- Gestionar credenciales mediante secretos y definir políticas de retención.

## 8. Respaldo y restauración de PostgreSQL

Se realizó un respaldo de la base de datos `clasificador` utilizando la herramienta `pg_dump` de PostgreSQL.

- Archivo generado: `respaldo-clasificador.sql`.
- Tamaño del archivo: aproximadamente 2,8 KB.
- Base de datos de origen: `clasificador`.

### 8.1 Prueba de restauración

Se creó una base de datos temporal llamada `clasificador_prueba` y se restauró el respaldo mediante `psql`.

La restauración finalizó sin errores. Posteriormente, se consultó la tabla `inferencias` y se confirmó la recuperación de un registro:

| ID | Mensaje | Categoría |
|---|---|---|
| 1 | fix: corregir error al iniciar sesión | fix |

**Resultado:** respaldo generado y restauración verificada correctamente. La base de datos original no fue modificada durante esta prueba.
