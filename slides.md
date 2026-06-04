---
marp: true
paginate: true
size: 16:9
lang: es
title: Applied AI
description: Presentación de ejemplo creada con Marp
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
  section::after {
    color: var(--muted);
    font-size: 18px;
  }
  footer { color: var(--muted); }
---

<!-- _class: lead -->
<!-- _paginate: false -->

# Applied AI

Una presentación de ejemplo creada con **Marp** y publicada en **GitHub Pages**

> Markdown → diapositivas, sin salir del editor

---

## ¿Qué es Marp?

**Marp** (*Markdown Presentation Ecosystem*) convierte Markdown en diapositivas.

- ✍️ Escribes en **Markdown** plano, separando slides con `---`
- 🎨 Temas y estilos con CSS, totalmente personalizables
- 📦 Exporta a **HTML**, **PDF** y **PowerPoint**
- 🔁 Diffs limpios en Git: la fuente es texto

> Ideal para versionar presentaciones junto a tu código.

---

## Cómo está hecha esta presentación

1. La fuente vive en **`slides.md`** (este mismo archivo)
2. Se compila a HTML con la CLI de Marp:

```bash
npx @marp-team/marp-cli@latest slides.md -o index.html --html
```

3. GitHub Pages sirve el `index.html` resultante 🚀

---

## Sintaxis básica

```markdown
---
marp: true
theme: default
paginate: true
---

# Primera diapositiva

---

## Segunda diapositiva
- Una viñeta
- Otra viñeta
```

Cada `---` empieza una **diapositiva nueva**.

---

<!-- _class: lead -->

# ¡Gracias! 🙌

Edita **`slides.md`** y recompila para actualizar el sitio

[ssoto.github.io/applied-ai](https://ssoto.github.io/applied-ai/)
