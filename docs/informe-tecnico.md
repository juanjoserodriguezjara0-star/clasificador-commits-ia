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

Las pruebas automatizadas sustituyen la llamada a Ollama por respuestas controladas para no depender de la red ni del tiempo de inferencia. También comprueban la validación de entradas y el tratamiento de errores. La integración real debe ejecutarse con Ollama y PostgreSQL activos.

No se presentan métricas de precisión ni tiempos de respuesta como resultados medidos hasta ejecutar un conjunto de evaluación definido.

## 6. Riesgos y limitaciones

- Un modelo pequeño puede clasificar incorrectamente mensajes ambiguos.
- La disponibilidad depende de Ollama y PostgreSQL.
- Las credenciales de ejemplo de Docker Compose son solo para desarrollo.
- Las pruebas unitarias no sustituyen una prueba de integración con los servicios reales.

## 7. Mejoras futuras

- Crear un conjunto etiquetado de mensajes y medir precisión, exhaustividad y F1 por categoría.
- Añadir autenticación, límites de solicitudes y observabilidad.
- Gestionar credenciales mediante secretos y definir políticas de retención.
