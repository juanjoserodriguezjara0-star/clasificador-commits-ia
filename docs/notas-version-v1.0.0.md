# Notas de versión: v1.0.0

## Alcance

Primera versión del clasificador de mensajes de commit con IA local.

## Funcionalidades

- API REST desarrollada con FastAPI.
- Clasificación de mensajes en `feat`, `fix`, `docs`, `test`, `chore` y `refactor`.
- Integración con Ollama mediante la API HTTP local.
- Persistencia de inferencias en PostgreSQL.
- Endpoints `GET /`, `GET /health`, `POST /clasificar` y `GET /inferencias`.
- Entorno de desarrollo con Docker Compose.
- Pruebas automatizadas con pytest y validaciones en GitHub Actions.
- README, manual técnico, informe técnico, script de preparación y script de diagnóstico.

## Validaciones confirmadas

La ejecución de GitHub Actions asociada al commit `8c6c399d804cf312f350a29fb93410a506c0ad46` terminó correctamente. Comprobó sintaxis Python, configuración de Docker Compose, construcción de la imagen Docker y pruebas de pytest.

Ejecución: https://github.com/juanjoserodriguezjara0-star/clasificador-commits-ia/actions/runs/39714272442

## Antes de publicar formalmente la release

- [ ] Ejecutar una prueba de integración con Ollama y PostgreSQL reales.
- [ ] Registrar evidencia de las seis categorías.
- [ ] Grabar y enlazar el video de demostración exigido por la guía.
- [ ] Obtener revisión de un compañero mediante pull request si así lo exige la guía.
- [ ] Confirmar que todos los requisitos de evaluación estén cubiertos.

Estas comprobaciones no se marcan como completadas hasta contar con evidencia real.
