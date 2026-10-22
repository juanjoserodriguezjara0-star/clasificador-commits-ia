# Manual técnico

## 1. Arquitectura

La solución expone una API REST con FastAPI. El endpoint de clasificación consulta un modelo local de Ollama y almacena la inferencia en PostgreSQL. Docker Compose permite levantar la API y la base de datos como servicios separados.

## 2. Requisitos

- Python 3.12 o Docker con Docker Compose.
- Ollama instalado y ejecutándose.
- Modelo `qwen2.5-coder:1.5b` descargado en Ollama.
- Para ejecución local sin contenedores: PostgreSQL accesible y una base inicializada con `db/init.sql`.

## 3. Configuración

Variables de entorno:

| Variable | Valor predeterminado | Uso |
|---|---|---|
| `OLLAMA_URL` | `http://localhost:11434` | URL de la API de Ollama |
| `OLLAMA_MODEL` | `qwen2.5-coder:1.5b` | Modelo usado para clasificar |
| `DATABASE_URL` | `postgresql://clasificador:clasificador@localhost:5432/clasificador` | Conexión a PostgreSQL |

En un entorno real, configura contraseñas seguras mediante variables de entorno. Las credenciales de ejemplo de Compose son únicamente para desarrollo local.

## 4. Ejecución con Docker Compose

1. Inicia Ollama en el equipo anfitrión y confirma que el modelo está disponible con `ollama list`.
2. Desde la raíz del proyecto, ejecuta `docker compose up --build -d`.
3. Revisa el estado con `docker compose ps` y los registros con `docker compose logs -f api`.
4. Abre `http://localhost:8000/docs` para probar la API.
5. Detén los servicios con `docker compose down`. Los datos permanecen en el volumen; para eliminarlos deliberadamente usa `docker compose down -v`.

Compose configura la URL de Ollama como `http://host.docker.internal:11434`. Si Ollama no acepta conexiones desde contenedores en tu sistema, ajusta la configuración de red de Ollama antes de usar la API.

## 5. Ejecución local con Python

Crea un entorno virtual, instala `requirements.txt`, configura `OLLAMA_URL` y `DATABASE_URL`, inicializa PostgreSQL con `db/init.sql` y ejecuta `uvicorn main:app --reload`. No ejecutes este modo a la vez que otro proceso usa el mismo puerto 8000.

## 6. Endpoints

### `GET /`
Devuelve un mensaje de estado y la versión de la API.

### `GET /health`
Informa si la API, Ollama y PostgreSQL responden. La respuesta puede indicar estado `degradado` si alguna dependencia no está disponible.

### `POST /clasificar`
Recibe un JSON como:

```json
{"mensaje": "fix: corregir error al iniciar sesión"}
```

Clasifica en una de estas etiquetas: `feat`, `fix`, `docs`, `test`, `chore` o `refactor`. Devuelve el identificador, el mensaje, la categoría y la fecha de creación. Si Ollama o PostgreSQL no están disponibles, devuelve un error HTTP explicativo.

### `GET /inferencias?limite=20`
Devuelve hasta 100 inferencias recientes. El parámetro `limite` acepta valores de 1 a 100.

## 7. Pruebas

Ejecuta `pytest -v`. Las pruebas unitarias sustituyen la llamada a Ollama por respuestas controladas para no depender de la red ni gastar tiempo de inferencia. La integración real requiere Ollama y PostgreSQL activos.

## 8. Solución de problemas

- **503 de Ollama:** verifica que Ollama esté activo, el modelo esté descargado y `OLLAMA_URL` sea accesible desde el contenedor.
- **503 de PostgreSQL:** revisa `docker compose ps`, `docker compose logs db` y la variable `DATABASE_URL`.
- **La tabla no existe:** confirma que `db/init.sql` se haya montado al inicializar la base. Los scripts de inicialización de PostgreSQL se ejecutan automáticamente solo cuando el directorio de datos se crea por primera vez.
- **El puerto está ocupado:** cambia el mapeo de puertos en Compose o detén el proceso que lo ocupa.
