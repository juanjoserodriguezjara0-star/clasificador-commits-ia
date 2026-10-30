# Investigación de modelos de inteligencia artificial en Ollama

## 1. Objetivo

Investigar tres modelos de lenguaje disponibles en Ollama con menos de 2.000 millones de parámetros y comparar sus características, licencias y aplicaciones.

## 2. Qwen2.5-Coder 1.5B

- Desarrollador: Alibaba Cloud.
- Parámetros: aproximadamente 1.54 mil millones.
- Tamaño: 986 MB.
- Licencia: Apache 2.0.
- Especialidad: programación y comprensión de código.
- Aplicaciones: generación, análisis y corrección de código.
- Estado: instalado y probado en nuestro proyecto.

Ficha oficial:
https://ollama.com/library/qwen2.5-coder:1.5b

## 3. DeepSeek-R1 1.5B

- Desarrollador: DeepSeek.
- Parámetros: aproximadamente 1.78 mil millones.
- Tamaño: 1.1 GB.
- Licencia: MIT para los pesos del modelo.
- Especialidad: razonamiento y resolución de problemas.
- Aplicaciones: matemáticas, programación y análisis lógico.
- Estado: investigado, no instalado ni probado.

Ficha oficial:
https://ollama.com/library/deepseek-r1:1.5b

## 4. SmolLM 1.7B

- Desarrollador: Hugging Face.
- Parámetros: aproximadamente 1.7 mil millones.
- Tamaño de descarga: aproximadamente 991 MB.
- Licencia: Apache 2.0.
- Especialidad: procesamiento y generación de texto.
- Aplicaciones: tareas generales de lenguaje y generación de respuestas.
- Estado: investigado, no instalado ni probado.

Limitación:
Está orientado principalmente al inglés. Se necesitarían pruebas adicionales para evaluar su desempeño en español.

Ficha oficial:
https://ollama.com/library/smollm:1.7b

## 5. Comparación de los modelos

| Característica | Qwen2.5-Coder | DeepSeek-R1 | SmolLM |
|---|---|---|---|
| Parámetros | 1.54B | 1.78B aprox. | 1.7B aprox. |
| Tamaño | 986 MB | 1.1 GB | 991 MB |
| Licencia | Apache 2.0 | MIT | Apache 2.0 |
| Especialidad | Programación | Razonamiento | Texto general |
| Instalado | Sí | No | No |

Los tamaños corresponden a las versiones consultadas y pueden variar según la cuantización.

## 6. Modelo seleccionado

Se seleccionó Qwen2.5-Coder 1.5B porque el proyecto clasifica mensajes de commits relacionados con el desarrollo de software.

Este modelo está especializado en programación, tiene un tamaño reducido y puede ejecutarse localmente.

Además, ya está instalado y conectado con FastAPI y PostgreSQL. Su integración fue comprobada mediante una clasificación real y el almacenamiento del resultado.

## 7. Conclusión

Los tres modelos investigados cumplen el requisito de tener menos de 2.000 millones de parámetros.

Qwen2.5-Coder es la alternativa seleccionada por su especialización en programación y su integración comprobada con nuestro proyecto.

DeepSeek-R1 y SmolLM son alternativas que podrían evaluarse posteriormente. No se afirma que sean mejores o peores, porque todavía no se han realizado pruebas comparativas con ellos.

## 8. Fuentes consultadas

- Qwen2.5-Coder:
  https://ollama.com/library/qwen2.5-coder:1.5b

- DeepSeek-R1:
  https://ollama.com/library/deepseek-r1:1.5b

- SmolLM:
  https://ollama.com/library/smollm:1.7b
