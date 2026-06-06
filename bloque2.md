---
marp: true
paginate: true
size: 16:9
lang: es
title: "Bloque 2 — Claude Cowork / Code"
description: "Flujos sin código y con código, automatizaciones reales con Claude"
theme: applied-ai
---

<!-- _class: lead -->
<!-- _paginate: false -->

# Bloque 2
## Claude Cowork / Code

Flujos sin código · Con código · Automatizaciones reales

---

## Dos velocidades de trabajo

| | Sin código | Con código |
|--|-----------|-----------|
| **Herramienta** | claude.ai, Projects | Claude Code CLI |
| **Perfil** | Cualquier rol | Desarrolladores |
| **Fuerza** | Velocidad, iteración | Automatización, integración |
| **Output** | Texto, análisis, ideas | Scripts, APIs, pipelines |

Ambos enfoques **se complementan** — elige según el problema.

---

## Flujos sin código

Con **claude.ai** puedes:

- Redactar y revisar documentos, correos, informes
- Analizar datos pegando CSV o tablas
- Resumir reuniones con transcripciones
- Crear plantillas y frameworks reutilizables con **Projects**

> Los **Projects** guardan contexto persistente — el modelo "recuerda" tu proyecto.

---

## Flujos con código — Claude Code

**Claude Code** es una CLI que convierte Claude en un agente de desarrollo:

```bash
# Instalar
npm install -g @anthropic-ai/claude-code

# Usar dentro de tu proyecto
cd mi-proyecto
claude
```

- Entiende el repositorio completo
- Escribe, edita, refactoriza y testea código
- Ejecuta comandos y lee resultados en tiempo real

---

## Automatizaciones reales

Casos de uso que ya están en producción:

- **Pipeline de contenido** — borrador → revisión → publicación
- **Code review asistido** — análisis automático de PRs
- **Extracción de datos** — PDFs, emails, documentos → estructurado
- **QA automatizado** — generar casos de test desde especificaciones

> El patrón: define la tarea en lenguaje natural, itera hasta que funcione.

---

<!-- _class: lead -->

# Demo en vivo 🖥️

Veamos Claude Code en acción

[← Volver al índice](index.html)
