# Clasificador de mensajes de commit con IA

API REST que clasifica mensajes de commit usando un modelo local de Ollama y guarda el resultado en PostgreSQL.

## Integrantes

- Dilan Guzmán
- Brigith León
- Juan Jara

## Categorías

| Etiqueta | Significado |
|---|---|
| `feat` | Nueva funcionalidad |
| `fix` | Corrección de errores |
| `docs` | Documentación |
| `test` | Pruebas |
| `chore` | Mantenimiento |
| `refactor` | Reorganización sin cambiar el comportamiento |

## Tecnologías

Python 3.12, FastAPI, Ollama (`qwen2.5-coder:1.5b`), PostgreSQL, Docker Compose, pytest y GitHub Actions.

## Requisitos

- Docker con Docker Compose.
- Ollama instalado en el equipo anfitrión.
- Modelo disponible: `ollama pull qwen2.5-coder:1.5b`.

## Inicio rápido con Docker

1. Asegúrate de que Ollama esté funcionando en el equipo anfitrión.
2. En la raíz del repositorio, ejecuta:

   ```bash
   docker compose up --build -d
   ```

3. Abre la documentación interactiva en [http://localhost:8000/docs](http://localhost:8000/docs).
4. Revisa el estado con `docker compose ps` y los registros con `docker compose logs -f api`.
5. Para detener los servicios: `docker compose down`.

La configuración Compose usa credenciales locales de desarrollo. No reutilices esas credenciales en un despliegue público.

## Endpoints

### `GET /`
Devuelve el mensaje de bienvenida y la versión.

### `GET /health`
Comprueba la disponibilidad de la API, Ollama y PostgreSQL. El campo `estado` puede ser `ok` o `degradado`.

### `POST /clasificar`
Ejemplo de entrada:

```json
{"mensaje": "fix: corregir error al iniciar sesión"}
```

El mensaje debe tener entre 1 y 2000 caracteres. La respuesta incluye el ID, el mensaje, la categoría y la fecha de creación. Las categorías posibles son `feat`, `fix`, `docs`, `test`, `chore` y `refactor`.

### `GET /inferencias?limite=20`
Consulta las inferencias más recientes. El límite debe estar entre 1 y 100.

## Pruebas automatizadas

Con Python 3.12:

```bash
python -m pip install -r requirements.txt
pytest -v
```

Las pruebas simulan Ollama y PostgreSQL cuando corresponde; no necesitan descargar ni ejecutar el modelo para validar la lógica de la API.

## Documentación adicional

- [Manual técnico](docs/manual-tecnico.md)
- [Informe técnico](docs/informe-tecnico.md)

## Limitaciones conocidas

La calidad de la clasificación depende del modelo y del mensaje recibido. Las métricas de precisión deben medirse con un conjunto de mensajes etiquetados; no se deben inventar resultados de evaluación.
