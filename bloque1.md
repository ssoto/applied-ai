---
marp: true
paginate: true
size: 16:9
lang: es
title: "Bloque 1 — Prompt Engineering"
description: "Técnicas de Prompt Engineering: zero-shot, few-shot, chain-of-thought"
theme: applied-ai
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

[← Volver al índice](index.html)
