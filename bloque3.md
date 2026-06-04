---
marp: true
paginate: true
size: 16:9
lang: es
title: "Bloque 3 — Claude SDK"
description: "API, modelos, tool use y primer agente funcional"
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

# Bloque 3
## Claude SDK

API · Modelos · Tool Use · Primer agente funcional

---

## La API de Anthropic

Acceso directo al modelo vía HTTP o SDK oficial.

```python
import anthropic

client = anthropic.Anthropic()

message = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hola, Claude"}]
)
print(message.content[0].text)
```

Disponible en **Python**, **TypeScript** y cualquier cliente HTTP.

---

## Modelos disponibles

| Modelo | ID | Caso de uso |
|--------|----|-------------|
| **Opus 4** | `claude-opus-4-8` | Razonamiento complejo |
| **Sonnet 4** | `claude-sonnet-4-6` | Balance rendimiento/coste |
| **Haiku 4** | `claude-haiku-4-5-...` | Velocidad, bajo coste |

> Regla práctica: empieza con **Sonnet**, escala a Opus si necesitas más razonamiento.

---

## Tool Use

Permite que el modelo **llame a funciones** definidas por ti.

```python
tools = [{
    "name": "get_weather",
    "description": "Obtiene el tiempo actual para una ciudad",
    "input_schema": {
        "type": "object",
        "properties": {"city": {"type": "string"}},
        "required": ["city"]
    }
}]
```

El modelo decide cuándo usar la herramienta — tú ejecutas la función y devuelves el resultado.

---

## Primer agente funcional

Un agente es un bucle: **razona → actúa → observa → repite**

```python
while True:
    response = client.messages.create(
        model="claude-sonnet-4-6",
        tools=tools,
        messages=messages
    )
    if response.stop_reason == "end_turn":
        break
    # ejecutar tool_use y añadir resultado a messages
    messages = handle_tool_calls(response, messages)
```

Con esto ya tienes un agente que puede **buscar, calcular y decidir**.

---

<!-- _class: lead -->

# Q&A y Próximos Pasos 🎯

---

## ¿Qué sigue?

- Explorar [console.anthropic.com](https://console.anthropic.com) — playground y créditos gratuitos
- Leer la [documentación de Tool Use](https://docs.anthropic.com/en/docs/tool-use)
- Construir tu propio agente esta semana
- Compartir lo que crees con el grupo

> El mejor aprendizaje es **construir algo real**.

---

<!-- _class: lead -->

# ¡Gracias! 🙌

Ha sido un placer aprender juntos
