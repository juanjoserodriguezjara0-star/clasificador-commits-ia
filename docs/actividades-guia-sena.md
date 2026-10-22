# Actividades complementarias de la guía SENA

Este documento organiza las actividades de contextualización y las evidencias que deben acompañar el proyecto integrador. No reemplaza los formularios ni las publicaciones que se deben entregar en Google Classroom.

## 1. Reflexión sobre el uso de IA local

Las organizaciones pueden preferir ejecutar modelos de inteligencia artificial en sus propios equipos cuando necesitan mayor control sobre sus datos, costos y disponibilidad. Al trabajar de forma local, la información puede permanecer dentro de la infraestructura de la empresa y no tiene que enviarse a un servicio externo para cada consulta. También es posible usar el modelo sin depender continuamente de una conexión a internet, siempre que el equipo tenga los recursos necesarios.

Sin embargo, ejecutar IA local no elimina todos los riesgos. La organización debe mantener los equipos, proteger el acceso, actualizar los programas y comprobar la calidad de las respuestas. Además, un modelo pequeño puede equivocarse o requerir más recursos de los disponibles. Por eso, una solución local necesita pruebas, documentación y supervisión antes de usarse en un proceso importante.

**Antes de entregar:** publicar esta reflexión en el tablón de Google Classroom y comentar la publicación de al menos un compañero, como pide la guía.

## 2. Cuestionario de conocimientos previos

La guía indica que se debe completar el formulario de entrada en Google Classroom sobre:
- Sistemas operativos Linux.
- Redes básicas.
- Bases de datos.
- Programación en Python.

El formulario es diagnóstico y no calificable. Debe diligenciarse directamente en Classroom.

## 3. Diagnóstico del computador

Registrar los datos reales del equipo antes de enviar el formulario de alistamiento:

| Dato solicitado | Dónde comprobarlo en Windows |
|---|---|
| Versión de Windows | Ejecutar `winver` |
| Memoria RAM total | Administrador de tareas → Rendimiento → Memoria |
| Tipo de disco | Administrador de tareas → Rendimiento → Disco |
| Virtualización | Administrador de tareas → Rendimiento → CPU |
| Espacio libre de la unidad C: | Explorador de archivos → Este equipo |

Requisitos mínimos para el camino local descrito por la guía: 4 GB de RAM, 15 GB libres, virtualización habilitada y Windows 10 versión 2004 o superior si se usa Windows. No completar estos campos con valores supuestos.

## 4. Mapa mental colaborativo

La guía pide relacionar estos conceptos y publicar el mapa en el tablón del aula:
- Desarrollo.
- Despliegue.
- Servidor.
- Contenedor.
- Modelo de lenguaje.
- Inferencia.
- Usuario final.

El equipo puede elaborarlo en draw.io, Excalidraw o una herramienta similar. La entrega debe incluir el archivo o una captura del mapa publicado.

## 5. Exploración de tres modelos de Ollama

Consultar el catálogo oficial: https://ollama.com/library

Seleccionar tres modelos con menos de 2 000 millones de parámetros. Registrar para cada uno:
1. Nombre y etiqueta exacta.
2. Tamaño de descarga indicado por el catálogo.
3. Licencia.
4. Tarea para la que fue diseñado.

No registrar tamaños ni licencias de memoria: deben verificarse en las páginas oficiales de cada modelo.

## 6. Proyecto integrador: estado de evidencias

| Evidencia | Estado |
|---|---|
| Repositorio compartido y estructura del proyecto | Avanzado; revisar estado actual en GitHub |
| README, manual técnico e informe técnico | Presentes en el repositorio |
| API FastAPI y categorías de commit | Implementadas en el repositorio |
| Pruebas automatizadas y GitHub Actions | Ejecución reciente aprobada |
| Dockerfile y Docker Compose | La CI valida la configuración y construye la imagen |
| Ollama y modelo local | Se reportó una respuesta correcta desde el equipo local |
| Integración real API + Ollama + PostgreSQL | Pendiente de ejecutar y documentar en el equipo |
| WSL2/Ubuntu y Docker instalados en el equipo | Pendiente de comprobar |
| Pull request revisado por un compañero | Pendiente; requiere revisión auténtica |
| Pruebas de carga con k6 y reporte de latencia | Pendiente de evidencia |
| Respaldo y restauración probados | Pendiente de evidencia |
| Release de GitHub `v1.0.0` | No publicar hasta validar la integración |
| Despliegue remoto y video de demostración | Pendiente de evidencia |

## 7. Orden recomendado para cerrar la entrega

1. Completar en Classroom la reflexión, el cuestionario y el formulario de caracterización del equipo.
2. Confirmar WSL2/Ubuntu, Docker Compose y el modelo de Ollama en el equipo.
3. Ejecutar el sistema completo y guardar resultados de `/health`, `/clasificar` y `/inferencias`.
4. Hacer pruebas de conectividad, seguridad y carga, y documentar resultados reales.
5. Solicitar revisión de un compañero mediante pull request.
6. Verificar el repositorio desde una copia limpia siguiendo el README.
7. Publicar el release `v1.0.0`, el despliegue remoto y el video cuando exista evidencia real.
