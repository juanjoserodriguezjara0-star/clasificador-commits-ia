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

## Pruebas de integración pendientes en un equipo con Ollama

- [ ] Confirmar que Ollama responde y que el modelo `qwen2.5-coder:1.5b` está instalado.
- [ ] Levantar PostgreSQL y verificar que se crea la tabla `inferencias`.
- [ ] Levantar la API y confirmar `GET /health`.
- [ ] Enviar mensajes representativos a `POST /clasificar` y comprobar las seis categorías.
- [ ] Confirmar que cada clasificación se guarda en PostgreSQL.
- [ ] Consultar los resultados con `GET /inferencias`.
- [ ] Probar el arranque completo mediante Docker Compose.
- [ ] Ejecutar `tests/load.js` con k6 y guardar resultados medidos.
- [ ] Crear un respaldo y probar su restauración en una base temporal.
- [ ] Registrar incidencias y resultados reales antes de declarar finalizada la integración.

## Revisión de entrega

- [ ] Confirmar los requisitos exactos de la guía del SENA.
- [ ] Obtener revisión de al menos un compañero mediante pull request, si la guía lo exige.
- [ ] Crear la etiqueta y la release de GitHub `v1.0.0` después de completar las pruebas pendientes.
- [ ] Añadir capturas o evidencia de ejecución real al informe, sin inventar resultados.
- [ ] Desplegar en un servidor remoto y enlazar el video de demostración, si corresponde a la entrega exigida.

## Criterio de aceptación

La versión se considera validada cuando las pruebas automáticas pasan, los servicios se ejecutan juntos correctamente y las evidencias de integración quedan registradas. Las pruebas unitarias por sí solas no demuestran que Ollama y PostgreSQL estén funcionando en el equipo de entrega.
