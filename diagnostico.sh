#!/usr/bin/env bash
set -u

echo "Diagnóstico del clasificador de commits"
echo "--------------------------------------"

if command -v python3 >/dev/null 2>&1; then
  echo "Python: $(python3 --version)"
else
  echo "ERROR: no se encontró python3"
fi

if command -v docker >/dev/null 2>&1; then
  echo "Docker: $(docker --version)"
  if docker compose version >/dev/null 2>&1; then
    echo "Docker Compose: disponible"
  else
    echo "AVISO: Docker Compose no está disponible"
  fi
else
  echo "AVISO: Docker no está instalado o no está en PATH"
fi

if command -v curl >/dev/null 2>&1; then
  if curl --silent --fail --max-time 3 http://localhost:11434/api/tags >/dev/null; then
    echo "Ollama: responde en http://localhost:11434"
  else
    echo "AVISO: Ollama no responde en http://localhost:11434"
  fi
fi

if curl --silent --fail --max-time 3 http://localhost:8000/health >/dev/null 2>&1; then
  echo "API: responde en http://localhost:8000"
else
  echo "API: todavía no responde en http://localhost:8000"
fi
