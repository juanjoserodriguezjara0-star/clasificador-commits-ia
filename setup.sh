#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$ROOT_DIR"

echo "Preparando el clasificador de commits con IA"
if ! command -v python3 >/dev/null 2>&1; then
  echo "ERROR: instala Python 3.12 o superior." >&2
  exit 1
fi

python3 -m venv .venv
# shellcheck disable=SC1091
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

if ! command -v ollama >/dev/null 2>&1; then
  echo "AVISO: Ollama no está en PATH. Instálalo desde https://ollama.com/."
elif ! ollama list | grep -q 'qwen2.5-coder:1.5b'; then
  echo "Descargando el modelo qwen2.5-coder:1.5b..."
  ollama pull qwen2.5-coder:1.5b
fi

echo
echo "Dependencias Python instaladas."
echo "Inicia la API con: source .venv/bin/activate && uvicorn main:app --reload"
echo "Diagnóstico: ./diagnostico.sh"
echo "La API requiere PostgreSQL inicializado y Ollama disponible."
