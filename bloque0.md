---
marp: true
paginate: true
size: 16:9
lang: es
title: "Bloque 0 — Bienvenida y Contexto"
description: "Bienvenida al taller Applied AI"
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

# Bloque 0
## Bienvenida y Contexto

Taller **Applied AI** · 15 min

---

## Agenda del día

| Bloque | Tema | Duración |
|--------|------|----------|
| **0** | Bienvenida y contexto | 15 min |
| **1** | Prompt Engineering | 60 min |
| **2** | Claude Cowork / Code | 60 min |
| **3** | Claude SDK | 60 min |
| — | Q&A y próximos pasos | 15 min |

---

## ¿Por qué Applied AI ahora?

- Los LLMs pasaron de **laboratorio** a **producción** en tiempo récord
- Las herramientas son accesibles sin necesidad de infraestructura propia
- El diferencial ya no es el modelo, sino **cómo lo usas**

> La IA aplicada no es una tendencia futura — es una habilidad presente.

---

## Qué veremos hoy

- **Prompt Engineering** — comunicarte con el modelo de forma efectiva
- **Claude Cowork / Code** — flujos reales con y sin código
- **Claude SDK** — construir tu primer agente funcional

Saldrás con **conocimiento práctico** y herramientas listas para usar.

---

<!-- _class: lead -->

# ¡Empecemos! 🚀

Cualquier pregunta, interrúmpeme cuando quieras
