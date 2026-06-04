---
marp: true
paginate: true
size: 16:9
lang: es
title: "Bloque 3 — Claude SDK"
description: "API, modelos, tool use y primer agente funcional"
theme: applied-ai
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
