# Lista de validación para la versión 1.0.0

Este documento distingue las comprobaciones automáticas realizadas de las que requieren ejecutar el sistema completo en un equipo.

## Comprobaciones automatizadas

- [x] GitHub Actions instala las dependencias.
- [x] GitHub Actions verifica la sintaxis de `main.py`.
- [x] GitHub Actions ejecuta las pruebas de pytest.
- [x] Las pruebas simulan las respuestas de Ollama y los errores de dependencias.
- [x] GitHub Actions valida Docker Compose y construye la imagen de la API.
- [x] Se añadió un script de prueba de humo con k6 para ejecutar contra una API disponible.

Consulta el estado de la ejecución más reciente en la pestaña Actions del repositorio.

## Pruebas de integración realizadas en el equipo local

- [x] Ollama respondió y el modelo `qwen2.5-coder:1.5b` estuvo disponible.
- [x] PostgreSQL inició correctamente y la tabla `inferencias` estuvo disponible.
- [x] La API respondió en `GET /health` con API, Ollama y PostgreSQL en estado `ok`.
- [x] Se envió un mensaje a `POST /clasificar`; el modelo devolvió una categoría válida.
- [x] La clasificación quedó guardada y fue consultable mediante `GET /inferencias`.
- [x] Los servicios se ejecutaron mediante Docker Compose.
- [x] `tests/load.js` se ejecutó con k6: 1 usuario virtual, 5 iteraciones, 5 solicitudes sin fallos, 10/10 comprobaciones y p95 de 6,33 ms. Esta es una prueba de humo, no una prueba de carga alta.
- [x] Se creó un respaldo y se restauró en `clasificador_restore_test`; se verificaron 3 registros.

Las pruebas anteriores se realizaron localmente el 25 de noviembre de 2026. El archivo de respaldo permanece local y no se incluye en el repositorio.

## Revisión de entrega

- [ ] Confirmar los requisitos exactos de la guía del SENA.
- [ ] Obtener revisión de al menos un compañero mediante pull request, si la guía lo exige.
- [ ] Crear la etiqueta y la release de GitHub `v1.0.0` después de completar las pruebas pendientes.
- [ ] Añadir capturas o evidencia de ejecución real al informe, sin inventar resultados.
- [ ] Desplegar en un servidor remoto y enlazar el video de demostración, si corresponde a la entrega exigida.

## Criterio de aceptación

La versión se considera validada cuando las pruebas automáticas pasan, los servicios se ejecutan juntos correctamente y las evidencias de integración quedan registradas. Las pruebas unitarias por sí solas no demuestran que Ollama y PostgreSQL estén funcionando en el equipo de entrega.
