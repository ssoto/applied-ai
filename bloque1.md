---
marp: true
paginate: true
size: 16:9
lang: es
title: "Bloque 1 — Prompt Engineering"
description: "Técnicas de Prompt Engineering: zero-shot, few-shot, chain-of-thought"
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

# Bloque 1
## Prompt Engineering

Zero-shot · Few-shot · Chain-of-Thought · Ejercicio práctico

---

## ¿Qué es un prompt?

Un **prompt** es la instrucción que le das al modelo para obtener una respuesta.

La calidad del output depende directamente de la **claridad y estructura** del input.

> "Garbage in, garbage out" — aplica igual a los LLMs.

---

## Zero-shot

El modelo responde **sin ejemplos previos**, solo con la instrucción.

```
Clasifica el sentimiento de esta frase como positivo, negativo o neutro:
"El servicio fue rápido pero la comida estaba fría."
```

- Simple y directo
- Funciona bien para tareas que el modelo conoce de su entrenamiento
- Límite: tareas muy específicas o con formato estricto

---

## Few-shot

Se añaden **ejemplos** (shots) antes de la tarea real.

```
Entrada: "Me encantó la experiencia" → Positivo
Entrada: "Tardaron demasiado"        → Negativo
Entrada: "Estuvo bien, sin más"      → Neutro

Entrada: "El producto llegó antes de lo esperado" → ?
```

- Enseña el formato y la lógica esperada
- Muy efectivo para clasificaciones y transformaciones personalizadas

---

## Chain-of-Thought (CoT)

Pedir al modelo que **razone paso a paso** antes de dar la respuesta final.

```
Resuelve el problema paso a paso:
Una tienda vende 3 camisetas a 15€ cada una con un 10% de descuento.
¿Cuánto paga el cliente en total?
```

> "Piensa paso a paso" o "Let's think step by step"

- Reduce errores en razonamiento matemático y lógico
- Especialmente útil en tareas complejas de múltiples pasos

---

## Ejercicio práctico

**Reto** — Reescribe este prompt para mejorar el resultado:

```
Resume esto.
```

Considera:
- ¿Cuál es el **rol** del modelo?
- ¿Qué **formato** quieres?
- ¿Qué **restricciones** tiene la respuesta?
- ¿Necesitas **ejemplos**?

---

<!-- _class: lead -->

# ¡Turno de práctica! ✍️

5 minutos para probar tu prompt en claude.ai
