---
marp: true
paginate: true
size: 16:9
lang: es
title: "Bloque 2 — Claude Cowork / Code"
description: "Flujos sin código y con código, automatizaciones reales con Claude"
theme: default
style: |
  :root {
    --bg: #0d1117;
    --fg: #e6edf3;
    --muted: #8b949e;
    --accent: #58a6ff;
    --accent-2: #a371f7;
    --card: #161b22;
    --border: #30363d;
  }
  section {
    background: var(--bg);
    color: var(--fg);
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
    padding: 70px 80px;
    font-size: 28px;
    line-height: 1.6;
  }
  h1, h2 { color: var(--fg); }
  h1 {
    font-size: 64px;
    background: linear-gradient(90deg, var(--accent), var(--accent-2));
    -webkit-background-clip: text;
    background-clip: text;
    color: transparent;
  }
  h2 { font-size: 44px; border-bottom: 2px solid var(--border); padding-bottom: .3em; }
  a { color: var(--accent); }
  strong { color: var(--accent); }
  code {
    background: var(--card);
    color: #79c0ff;
    border-radius: 6px;
    padding: .1em .4em;
  }
  pre code { display: block; padding: 1em; border: 1px solid var(--border); }
  blockquote {
    border-left: 4px solid var(--accent-2);
    color: var(--muted);
    padding-left: 1em;
    font-style: italic;
  }
  ul li::marker { color: var(--accent); }
  section.lead { justify-content: center; text-align: center; }
  section.lead p { color: var(--muted); font-size: 32px; }
  section::after { color: var(--muted); font-size: 18px; }
  footer { color: var(--muted); }
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
