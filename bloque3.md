---
marp: true
paginate: true
size: 16:9
lang: es
title: "Bloque 3 — Claude SDK"
description: "API, modelos, tool use y primer agente funcional"
theme: applied-ai
---

<script>
(function () {
  function inject() {
    const osc = document.querySelector('.bespoke-marp-osc');
    if (!osc || osc.querySelector('#home-btn')) return;
    const btn = document.createElement('a');
    btn.id = 'home-btn';
    btn.href = 'index.html';
    btn.title = 'Volver al inicio';
    btn.textContent = '⌂';
    btn.style.cssText = 'opacity:.8;cursor:pointer;font-size:2.4em;color:inherit;text-decoration:none;padding:0 4px;transition:opacity .2s';
    btn.onmouseenter = () => btn.style.opacity = '1';
    btn.onmouseleave = () => btn.style.opacity = '.8';
    osc.appendChild(btn);
  }
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', inject);
  } else {
    inject();
  }
})();
</script>

<!-- _class: lead -->
<!-- _paginate: false -->

# Bloque 3
## Claude SDK

API · Modelos · Tool Use · Primer agente funcional

---

## ¿Qué vamos a ver?

1. **¿Por qué el SDK?** — cuándo pasar de herramientas a código
2. **Hello World** — tu primera llamada en Python
3. **Tool Use** — Claude conectado a tus datos reales
4. **El agente** — bucle de razonamiento y acción
5. **Ejercicio práctico** — construye el agente de tu startup
6. **De demo a producción** — costes, errores y deployment

> Al final tendrás un agente funcional que resuelve **un problema real**.

---

<!-- _class: lead -->

# ¿Por qué el SDK?

---

## La escalera de herramientas

<svg viewBox="0 0 1060 360" xmlns="http://www.w3.org/2000/svg" width="100%" style="display:block;margin-top:0.2em">
  <defs>
    <linearGradient id="sg" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#2dd4bf"/>
      <stop offset="100%" stop-color="#7c6bff"/>
    </linearGradient>
  </defs>
  <!-- Y-axis label -->
  <text transform="rotate(-90,14,247)" x="14" y="247" text-anchor="middle" fill="#7a7890" font-size="11" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif">Automatización ↑</text>
  <!-- Staircase -->
  <path d="M 25,345 H 285 V 280 H 535 V 215 H 785 V 150 H 1045" stroke="url(#sg)" stroke-width="2.5" fill="none" stroke-linejoin="round" stroke-linecap="round"/>
  <!-- Card 1: Claude.ai -->
  <rect x="45" y="240" width="210" height="105" rx="10" fill="#17161e" stroke="#2d2b3a" stroke-width="1"/>
  <text x="150" y="267" text-anchor="middle" fill="#f0eeff" font-size="15" font-weight="700" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif">Claude.ai</text>
  <text x="150" y="287" text-anchor="middle" fill="#7a7890" font-size="11" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif">Chat en el navegador</text>
  <rect x="85" y="297" width="130" height="22" rx="5" fill="none" stroke="#2dd4bf" stroke-width="1"/>
  <text x="150" y="312" text-anchor="middle" fill="#2dd4bf" font-size="10.5" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif">Sin instalación</text>
  <!-- Card 2: Cowork -->
  <rect x="305" y="175" width="210" height="105" rx="10" fill="#17161e" stroke="#2d2b3a" stroke-width="1"/>
  <text x="410" y="202" text-anchor="middle" fill="#f0eeff" font-size="15" font-weight="700" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif">Cowork</text>
  <text x="410" y="222" text-anchor="middle" fill="#7a7890" font-size="11" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif">Tus archivos + Claude</text>
  <rect x="345" y="232" width="130" height="22" rx="5" fill="none" stroke="#2dd4bf" stroke-width="1"/>
  <text x="410" y="247" text-anchor="middle" fill="#2dd4bf" font-size="10.5" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif">Sin código</text>
  <!-- Card 3: Claude Code -->
  <rect x="555" y="110" width="210" height="105" rx="10" fill="#17161e" stroke="#2d2b3a" stroke-width="1"/>
  <text x="660" y="137" text-anchor="middle" fill="#f0eeff" font-size="15" font-weight="700" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif">Claude Code</text>
  <text x="660" y="157" text-anchor="middle" fill="#7a7890" font-size="11" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif">Claude en tu terminal</text>
  <rect x="595" y="167" width="130" height="22" rx="5" fill="none" stroke="#7c6bff" stroke-width="1"/>
  <text x="660" y="182" text-anchor="middle" fill="#7c6bff" font-size="10.5" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif">CLI</text>
  <!-- Card 4: SDK/API (highlighted) -->
  <rect x="805" y="45" width="210" height="105" rx="10" fill="#17161e" stroke="#7c6bff" stroke-width="1.5"/>
  <text x="910" y="72" text-anchor="middle" fill="#f0eeff" font-size="15" font-weight="700" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif">SDK / API</text>
  <text x="910" y="92" text-anchor="middle" fill="#7a7890" font-size="11" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif">Claude en tu producto</text>
  <rect x="845" y="102" width="130" height="22" rx="5" fill="#7c6bff"/>
  <text x="910" y="117" text-anchor="middle" fill="white" font-size="10.5" font-weight="600" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif">Código</text>
  <!-- X-axis label -->
  <text x="535" y="357" text-anchor="middle" fill="#7a7890" font-size="11" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif">Conocimiento técnico requerido →</text>
</svg>

---

## Cuándo necesitas el SDK

**Usa Claude.ai / Cowork** cuando el trabajo es manual, puntual, tú y tu equipo.

**Usa el SDK cuando:**

- El proceso debe correr **sin que nadie lo active** — a las 8h, al recibir un email, al registrarse un usuario
- Claude necesita consultar **tu base de datos**, no conocimiento genérico
- Quieres integrar IA en **tu producto** — tus usuarios ven tu app, no Claude
- Necesitas escalar a **miles de llamadas** sin intervención humana

> Las respuestas del formulario de hoy son exactamente este tipo de problema.

---

<!-- _class: lead -->

# Hello World

---

## Setup en 3 pasos

<style scoped>
.steps { display: flex; flex-direction: column; gap: 0.9em; margin-top: 1em; }
.step { display: flex; gap: 1em; align-items: flex-start; }
.num { background: var(--accent); color: white; border-radius: 50%; min-width: 2em; height: 2em; display: flex; align-items: center; justify-content: center; font-weight: 700; flex-shrink: 0; }
.body { background: var(--card); border-radius: 10px; padding: 0.7em 1em; flex: 1; font-size: 0.85em; line-height: 1.6; }
.body strong { color: var(--accent); }
</style>

<div class="steps">
<div class="step">
  <div class="num">1</div>
  <div class="body"><strong>Crea un entorno virtual</strong><br><code>python -m venv .venv && source .venv/bin/activate</code> — aísla las dependencias del proyecto del resto del sistema.</div>
</div>
<div class="step">
  <div class="num">2</div>
  <div class="body"><strong>Instala la librería oficial</strong><br><code>pip install anthropic</code> dentro del entorno. Sin dependencias pesadas.</div>
</div>
<div class="step">
  <div class="num">3</div>
  <div class="body"><strong>Configura tu API key</strong><br>Exporta <code>ANTHROPIC_API_KEY</code> como variable de entorno. El cliente la lee automáticamente al instanciarlo — no hay que pasarla en el código.</div>
</div>
</div>

Consigue tu key gratuita en **console.anthropic.com** — incluye créditos para empezar.

---

## Modelos disponibles

| Modelo | ID | Velocidad | Cuándo usarlo |
|--------|----|-----------|---------------|
| **Haiku 4** | `claude-haiku-4-5-...` | ⚡⚡⚡ | Clasificación, resúmenes, volumen alto |
| **Sonnet 4** | `claude-sonnet-4-6` | ⚡⚡ | La mayoría de casos — **empieza aquí** |
| **Opus 4** | `claude-opus-4-8` | ⚡ | Razonamiento complejo, análisis profundo |

> Regla práctica: **Sonnet** para tareas complejas, **Haiku** cuando necesites velocidad y tareas simples.

---

## Tu primera llamada

<style scoped>
.params { display: grid; grid-template-columns: auto 1fr; gap: 0.5em 1em; margin-top: 0.9em; font-size: 0.83em; align-items: start; }
.param { background: var(--accent-2); color: white; border-radius: 5px; padding: 0.1em 0.55em; font-family: monospace; font-weight: 600; white-space: nowrap; margin-top: 0.2em; }
.desc { background: var(--card); border-radius: 6px; padding: 0.3em 0.8em; line-height: 1.55; }
</style>

Se llama a `client.messages.create()` con tres parámetros clave:

<div class="params">
  <div class="param">model</div><div class="desc">Qué versión de Claude usar — <code>claude-haiku-4-5</code> para empezar.</div>
  <div class="param">max_tokens</div><div class="desc">Límite máximo de tokens en la respuesta. Controla el coste y evita respuestas infinitas.</div>
  <div class="param">messages</div><div class="desc">Array con el historial de la conversación. El primer mensaje es siempre <code>role: "user"</code> con tu pregunta.</div>
</div>

La respuesta llega en `response.content[0].text` — exactamente el mismo texto que verías en Claude.ai, pero ahora **dentro de tu código**.

<p style="font-size:0.65em;color:#7a7890;margin-top:auto">▶ <a href="https://github.com/ssoto/applied-ai/blob/main/sdk_examples/01_primera_llamada.py" target="_blank" style="color:inherit">sdk_examples/01_primera_llamada.py</a></p>

---

## Conversación multi-turno

<style scoped>
.calls { display: flex; flex-direction: column; gap: 0.55em; margin-top: 0.5em; }
.call { display: grid; grid-template-columns: auto 1fr; gap: 0 0.8em; align-items: start; }
.badge { background: var(--accent); color: white; border-radius: 6px; padding: 0.15em 0.55em; font-size: 0.72em; font-weight: 700; white-space: nowrap; margin-top: 0.35em; }
.badge.r2 { background: var(--accent-2); }
.msgs { background: var(--card); border-radius: 8px; padding: 0.4em 0.8em; font-size: 0.72em; line-height: 1.7; font-family: monospace; }
.u { color: var(--accent); } .a { color: var(--accent-2); } .dim { color: #666; }
</style>

<div class="calls">
<div class="call">
  <div class="badge">1ª llamada</div>
  <div class="msgs">
    messages = [<span class="u">{ role:"user", content:"¿Qué ejercicio me recomiendas?" }</span>]<br>
    <span class="dim">→ Claude responde: "Te recomiendo empezar con 20 min de cardio suave..."</span>
  </div>
</div>
<div class="call">
  <div class="badge r2">2ª llamada</div>
  <div class="msgs">
    messages = [<span class="u">{ role:"user",      content:"¿Qué ejercicio me recomiendas?" }</span>,<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="a">{ role:"assistant", content:"Te recomiendo empezar con 20 min de cardio..." }</span>,<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="u">{ role:"user",      content:"¿Y si solo tengo 10 minutos?" }</span>]<br>
    <span class="dim">→ Claude recuerda el contexto: "Con 10 minutos, prueba HIIT: 30s esfuerzo / 30s descanso × 10..."</span>
  </div>
</div>
</div>

> Cada llamada es **sin estado** — la memoria eres tú: añade las respuestas anteriores al array `messages`.

---

<!-- _class: lead -->

# Tool Use

Claude conectado a tus datos reales

---

## Claude como orquestador

<style scoped>
.flow { display: grid; grid-template-columns: 1fr auto 1fr auto 1fr; align-items: center; gap: 0.5em; margin-top: 1.5em; text-align: center; }
.box { background: var(--card); border: 1px solid var(--border); border-radius: 12px; padding: 1em 0.6em; font-size: 0.82em; line-height: 1.6; }
.box strong { display: block; font-size: 1em; color: var(--accent); margin-bottom: 0.2em; }
.arrow { font-size: 1.8em; color: var(--accent-2); }
</style>

<div class="flow">
<div class="box"><strong>Tu app</strong>pregunta del usuario</div>
<div class="arrow">⇆</div>
<div class="box"><strong>Claude</strong>razona y decide qué herramienta usar y cuándo</div>
<div class="arrow">⇆</div>
<div class="box"><strong>Tus funciones</strong>tu BD, tu API, tus datos reales</div>
</div>

**Sin Tool Use:** Claude responde con conocimiento genérico.  
**Con Tool Use:** Claude responde con **tus datos reales**.

> Claude decide **cuándo** llamar la herramienta. Tú defines **qué hace**.

---

## Anatomía de una herramienta

<style scoped>
.fields { display: flex; flex-direction: column; gap: 0.6em; margin-top: 0.8em; }
.field { display: grid; grid-template-columns: auto 1fr; gap: 0 1em; align-items: start; }
.key { background: var(--accent-2); color: white; border-radius: 5px; padding: 0.15em 0.6em; font-family: monospace; font-weight: 600; font-size: 0.82em; white-space: nowrap; margin-top: 0.25em; }
.val { background: var(--card); border-radius: 6px; padding: 0.3em 0.85em; font-size: 0.83em; line-height: 1.6; }
</style>

Una herramienta es un diccionario con tres campos:

<div class="fields">
  <div class="field">
    <div class="key">name</div>
    <div class="val">Identificador que Claude usa para invocar la función. Debe ser único y descriptivo — por ejemplo <code>"buscar_usuario"</code>.</div>
  </div>
  <div class="field">
    <div class="key">description</div>
    <div class="val">Texto en lenguaje natural <strong>dirigido a Claude</strong> — explica qué hace la función y cuándo usarla. Es el campo más importante: de él depende que Claude elija bien.</div>
  </div>
  <div class="field">
    <div class="key">input_schema</div>
    <div class="val">JSON Schema con los parámetros que acepta: tipo, nombre y descripción de cada uno. Claude los infiere y rellena automáticamente según el contexto.</div>
  </div>
</div>

<p style="font-size:0.65em;color:#7a7890;margin-top:auto">▶ <a href="https://github.com/ssoto/applied-ai/blob/main/sdk_examples/02_tool_definition.py" target="_blank" style="color:inherit">sdk_examples/02_tool_definition.py</a></p>

---

## El flujo de Tool Use — paso a paso

<style scoped>
.steps { display: flex; flex-direction: column; gap: 0.5em; margin-top: 0.8em; }
.step { display: flex; align-items: center; gap: 0.8em; font-size: 0.83em; }
.num { background: var(--accent); color: white; border-radius: 50%; width: 1.8em; height: 1.8em; display: flex; align-items: center; justify-content: center; font-weight: bold; flex-shrink: 0; font-size: 0.9em; }
.content { background: var(--card); border-radius: 8px; padding: 0.4em 0.9em; flex: 1; }
</style>

<div class="steps">
<div class="step"><div class="num">1</div><div class="content">Usuario pregunta: <em>"¿Cuál es el plan de entrenamiento de María?"</em></div></div>
<div class="step"><div class="num">2</div><div class="content">Claude recibe la pregunta y la lista de herramientas disponibles</div></div>
<div class="step"><div class="num">3</div><div class="content">Claude responde con <code>tool_use</code>: "quiero llamar <code>buscar_usuario("María")</code>"</div></div>
<div class="step"><div class="num">4</div><div class="content">Tu código ejecuta la función real y obtiene el resultado de la BD</div></div>
<div class="step"><div class="num">5</div><div class="content">Devuelves el resultado a Claude como <code>tool_result</code></div></div>
<div class="step"><div class="num">6</div><div class="content">Claude genera la respuesta final usando los datos reales</div></div>
</div>

---

## Tool Use y Tool Result en las llamadas

<style scoped>
.calls { display: flex; flex-direction: column; gap: 0.55em; margin-top: 0.5em; }
.call { display: grid; grid-template-columns: auto 1fr; gap: 0 0.8em; align-items: start; }
.badge { background: var(--accent); color: white; border-radius: 6px; padding: 0.15em 0.55em; font-size: 0.72em; font-weight: 700; white-space: nowrap; margin-top: 0.35em; }
.badge.r2 { background: var(--accent-2); }
.msgs { background: var(--card); border-radius: 8px; padding: 0.4em 0.8em; font-size: 0.70em; line-height: 1.7; font-family: monospace; }
.u { color: var(--accent); } .a { color: var(--accent-2); } .t { color: #f59e0b; } .dim { color: #666; }
</style>

<div class="calls">
<div class="call">
  <div class="badge">1ª llamada</div>
  <div class="msgs">
    messages = [<span class="u">{ role:"user", content:"¿Cuál es el plan de María?" }</span>]<br>
    <span class="dim">→ stop_reason: "tool_use"</span><br>
    <span class="a">{ role:"assistant", content:[{ type:<span class="t">"tool_use"</span>, id:"tu_01", name:"buscar_usuario", input:{nombre:"María"} }] }</span>
  </div>
</div>
<div class="call">
  <div class="badge r2">2ª llamada</div>
  <div class="msgs">
    messages = [ …turno anterior…,<br>
    &nbsp;&nbsp;<span class="u">{ role:"user", content:[{ type:<span class="t">"tool_result"</span>, tool_use_id:"tu_01", content:"{id:'u123', nivel:'intermedio'}" }] }</span>]<br>
    <span class="dim">→ stop_reason: "end_turn" → Claude genera la respuesta final</span>
  </div>
</div>
</div>

> `tool_use` es Claude pidiendo ejecutar algo. `tool_result` eres tú devolviendo el dato. **Siempre en el array `messages`.**

---

<!-- _class: lead -->

# El Agente

El bucle que todo lo une

---

## El loop del agente

<style scoped>
.ann { display: flex; flex-direction: column; gap: 0.55em; margin-top: 0.6em; }
.row { display: flex; gap: 0.7em; align-items: flex-start; font-size: 0.83em; line-height: 1.55; }
.num { color: white; border-radius: 50%; min-width: 1.7em; height: 1.7em; display: flex; align-items: center; justify-content: center; font-weight: 700; font-size: 0.85em; flex-shrink: 0; margin-top: 0.1em; }
.nb { background: var(--accent); }
.nt { background: var(--accent-2); }
.nok { background: #22c55e; }
.txt { background: var(--card); border-radius: 6px; padding: 0.35em 0.85em; flex: 1; }
</style>

<div class="ann">
<div class="row"><div class="num nb">1</div><div class="txt">Inicializa el historial con la pregunta del usuario como primer mensaje.</div></div>
<div class="row"><div class="num nb">2</div><div class="txt">Llama a la API pasando el historial completo, el system prompt y la lista de tools disponibles.</div></div>
<div class="row"><div class="num nb">3</div><div class="txt">Añade la respuesta de Claude al historial — sea texto final o una petición de tool.</div></div>
<div class="row"><div class="num nok">4</div><div class="txt"><strong>Si <code>stop_reason == "end_turn"</code></strong>: Claude considera que tiene suficiente información y ha generado una respuesta completa — no necesita llamar a ninguna tool más. Sale del loop y mostramos el texto al usuario. El otro valor posible es <code>"tool_use"</code>: Claude quiere datos antes de responder.</div></div>
<div class="row"><div class="num nt">5</div><div class="txt"><strong>Si <code>stop_reason == "tool_use"</code></strong>: recorre los bloques de la respuesta, ejecuta cada tool con tus datos reales y recoge los resultados.</div></div>
<div class="row"><div class="num nt">6</div><div class="txt">Devuelve los resultados como <code>tool_result</code> en el historial y vuelve al paso 2 — Claude decide si necesita más tools o puede responder.</div></div>
</div>

<p style="font-size:0.65em;color:#7a7890;margin-top:auto">▶ <a href="https://github.com/ssoto/applied-ai/blob/main/sdk_examples/03_fitcoach_agent.py" target="_blank" style="color:inherit">sdk_examples/03_fitcoach_agent.py</a></p>

---

## FitCoach — definir las herramientas

<style scoped>
.tools { display: grid; grid-template-columns: 1fr 1fr; gap: 1em; margin-top: 0.8em; }
.tool { background: var(--card); border: 1px solid var(--border); border-radius: 10px; padding: 0.8em 1em; font-size: 0.82em; line-height: 1.6; }
.tool strong { color: var(--accent); font-family: monospace; display: block; margin-bottom: 0.3em; font-size: 1.05em; }
.tool .param { color: var(--accent-2); font-family: monospace; font-size: 0.9em; }
</style>

Se definen **dos herramientas** que Claude puede invocar:

<div class="tools">
<div class="tool">
  <strong>buscar_usuario(nombre)</strong>
  Recibe el nombre completo del usuario y devuelve su <span class="param">id</span>, <span class="param">nivel</span> y <span class="param">objetivo</span>.<br>
  Claude la usa cuando necesita identificar a alguien antes de consultar su plan.
</div>
<div class="tool">
  <strong>obtener_plan(usuario_id)</strong>
  Recibe el <span class="param">usuario_id</span> y devuelve el plan: días, minutos de cardio y de fuerza.<br>
  Claude la usa una vez tiene el id del usuario obtenido con la tool anterior.
</div>
</div>

> Las descripciones guían a Claude para encadenar las tools en el orden correcto sin instrucciones explícitas.

<p style="font-size:0.65em;color:#7a7890;margin-top:auto">▶ <a href="https://github.com/ssoto/applied-ai/blob/main/sdk_examples/03_fitcoach_agent.py" target="_blank" style="color:inherit">sdk_examples/03_fitcoach_agent.py</a></p>

---

## La memoria del agente — el historial

<style scoped>
.history { display: flex; flex-direction: column; gap: 0.35em; margin-top: 0.5em; }
.msg { display: flex; gap: 0.7em; align-items: flex-start; font-size: 0.78em; }
.role { font-weight: bold; color: var(--accent); min-width: 5.5em; padding-top: 0.3em; }
.content { background: var(--card); border-radius: 6px; padding: 0.3em 0.8em; flex: 1; line-height: 1.6; }
.tool-call { color: var(--accent-2); }
.tool-result { color: #888; }
</style>

<div class="history">
<div class="msg"><div class="role">user</div><div class="content">"¿Cuál es el plan de María García?"</div></div>
<div class="msg"><div class="role">assistant</div><div class="content tool-call">tool_use → buscar_usuario("María García")</div></div>
<div class="msg"><div class="role">user</div><div class="content tool-result">tool_result → {id: "u123", nivel: "intermedio", objetivo: "resistencia"}</div></div>
<div class="msg"><div class="role">assistant</div><div class="content tool-call">tool_use → obtener_plan("u123")</div></div>
<div class="msg"><div class="role">user</div><div class="content tool-result">tool_result → {días: ["lun", "mié", "vie"], cardio: "30 min", fuerza: "45 min"}</div></div>
<div class="msg"><div class="role">assistant</div><div class="content">"María sigue un plan de 3 días por semana enfocado en resistencia..."</div></div>
</div>

> El historial **es** la memoria del agente — cada turno Claude ve todo el contexto anterior.

---

## FitCoach — ejecutar las herramientas

<style scoped>
.cols { display: grid; grid-template-columns: 1fr 1fr; gap: 1em; margin-top: 0.8em; }
.box { background: var(--card); border-radius: 10px; padding: 0.8em 1em; font-size: 0.82em; line-height: 1.6; }
.box strong { color: var(--accent); display: block; margin-bottom: 0.3em; }
</style>

<div class="cols">
<div class="box">
  <strong>Datos simulados</strong>
  Dos diccionarios Python replican lo que haría una base de datos real: uno con perfiles de usuario y otro con planes de entrenamiento indexados por <code>usuario_id</code>.
</div>
<div class="box">
  <strong>Dispatcher <code>ejecutar_tool</code></strong>
  Una sola función recibe el nombre de la tool y sus parámetros, y delega a la lógica correspondiente. En producción aquí iría la consulta SQL o la llamada a tu API.
</div>
</div>

Si Claude solicita un usuario que no existe, la función devuelve `{"error": "Usuario no encontrado"}` — Claude recibe ese mensaje y puede adaptar su respuesta al usuario final.

<p style="font-size:0.65em;color:#7a7890;margin-top:auto">▶ <a href="https://github.com/ssoto/applied-ai/blob/main/sdk_examples/03_fitcoach_agent.py" target="_blank" style="color:inherit">sdk_examples/03_fitcoach_agent.py</a></p>

---

## FitCoach — en acción

<style scoped>
section { font-size: 0.92em; }
.demo { background: var(--card); border-radius: 12px; padding: 1em 1.4em; margin-top: 0.8em; line-height: 2; font-size: 0.83em; }
.user { color: var(--accent); font-weight: bold; }
.agent { color: var(--accent-2); font-weight: bold; }
.tool { color: #888; font-style: italic; }
</style>

<div class="demo">
<span class="user">Usuario:</span> "¿Cuál es el plan de entrenamiento de María García?"<br>
<span class="tool">→ Claude llama buscar_usuario("María García") → {id: "u123", nivel: "intermedio"}</span><br>
<span class="tool">→ Claude llama obtener_plan("u123") → {días: ["lun","mié","vie"], cardio: "30 min"}</span><br>
<span class="agent">FitCoach:</span> "María sigue un plan de 3 días por semana (lunes, miércoles y viernes), enfocado en resistencia. Cada sesión incluye 30 min de cardio y 45 min de fuerza — adecuado para su nivel intermedio."
</div>

> Claude coordinó dos llamadas, combinó los resultados y generó una respuesta contextualizada — todo automático.

<p style="font-size:0.65em;color:#7a7890;margin-top:auto">▶ <a href="https://github.com/ssoto/applied-ai/blob/main/sdk_examples/03_fitcoach_agent.py" target="_blank" style="color:inherit">sdk_examples/03_fitcoach_agent.py</a></p>

---

## El agent loop — vuelta a vuelta

<style scoped>
.loop { display: flex; flex-direction: column; gap: 0.4em; margin-top: 0.4em; }
.iter { display: grid; grid-template-columns: auto 1fr; gap: 0 0.8em; align-items: start; }
.badge { border-radius: 6px; padding: 0.15em 0.55em; font-size: 0.70em; font-weight: 700; white-space: nowrap; margin-top: 0.35em; text-align: center; }
.b1 { background: var(--accent); color: white; }
.b2 { background: var(--accent-2); color: white; }
.b3 { background: #22c55e; color: white; }
.msgs { background: var(--card); border-radius: 8px; padding: 0.35em 0.8em; font-size: 0.68em; line-height: 1.65; font-family: monospace; }
.u { color: var(--accent); } .a { color: var(--accent-2); } .t { color: #f59e0b; } .ok { color: #22c55e; } .dim { color: #666; }
.arrow { text-align: center; color: var(--border); font-size: 0.9em; margin-left: 5.5em; }
</style>

<div class="loop">
<div class="iter">
  <div class="badge b1">iter 1</div>
  <div class="msgs">
    <span class="dim">while True → </span>client.messages.create(messages)<br>
    <span class="a">assistant → [{ type:<span class="t">"tool_use"</span>, name:"buscar_usuario", id:"tu_01" }]</span>&nbsp;&nbsp;<span class="dim">stop_reason: "tool_use"</span><br>
    <span class="u">user&nbsp;&nbsp;&nbsp;&nbsp; ← [{ type:<span class="t">"tool_result"</span>, tool_use_id:"tu_01", content:"{id:'u123'…}" }]</span>
  </div>
</div>
<div class="arrow">↓ loop continúa</div>
<div class="iter">
  <div class="badge b2">iter 2</div>
  <div class="msgs">
    <span class="dim">while True → </span>client.messages.create(messages) &nbsp;<span class="dim">(ahora con 3 mensajes)</span><br>
    <span class="a">assistant → [{ type:<span class="t">"tool_use"</span>, name:"obtener_plan", id:"tu_02" }]</span>&nbsp;&nbsp;<span class="dim">stop_reason: "tool_use"</span><br>
    <span class="u">user&nbsp;&nbsp;&nbsp;&nbsp; ← [{ type:<span class="t">"tool_result"</span>, tool_use_id:"tu_02", content:"{días:…}" }]</span>
  </div>
</div>
<div class="arrow">↓ loop continúa</div>
<div class="iter">
  <div class="badge b3">iter 3</div>
  <div class="msgs">
    <span class="dim">while True → </span>client.messages.create(messages) &nbsp;<span class="dim">(ahora con 5 mensajes)</span><br>
    <span class="a">assistant → "María sigue un plan de 3 días…"</span>&nbsp;&nbsp;<span class="ok">stop_reason: "end_turn" → break ✓</span>
  </div>
</div>
</div>

---

# Manos a la obra 🛠️

<style scoped>
section { font-size: 0.97em; }
.cols { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 1.2em; margin-top: 0.6em; }
.col { background: var(--card); border: 1px solid var(--border); border-radius: 12px; padding: 1em 1.2em; }
.col h3 { margin-top: 0; font-size: 0.88em; }
.col p, .col ul { font-size: 0.77em; line-height: 1.7; margin: 0.2em 0; }
.col code { font-size: 0.85em; }
</style>

<div class="cols">
<div class="col">

### 🎓 Plataforma educativa

**Tools:**
`obtener_curriculum(materia)`
`generar_pregunta(tema, nivel)`

**Objetivo:** agente que genera una batería de preguntas para un tema concreto, adaptadas al nivel del alumno

</div>
<div class="col">

### 💪 Fitness / operaciones

**Tools:**
`buscar_usuario(nombre)`
`actualizar_plan(usuario_id, cambios)`

**Objetivo:** agente que recibe una solicitud de cambio y actualiza el plan automáticamente

</div>
<div class="col">

### 💬 Atención al cliente

**Tools:**
`buscar_pedido(numero)`
`escalar_ticket(pedido_id, motivo)`

**Objetivo:** agente que responde preguntas con datos reales del pedido y escala si no puede resolver

</div>
</div>

**Entregable:** define las 2 tools de tu caso (nombre, descripción, parámetros) y el system prompt.

---

## Template base — adapta a tu caso

<style scoped>
.parts { display: flex; flex-direction: column; gap: 0.6em; margin-top: 0.8em; }
.part { display: flex; gap: 0.8em; align-items: flex-start; font-size: 0.83em; }
.tag { background: var(--accent-2); color: white; border-radius: 5px; padding: 0.1em 0.55em; font-family: monospace; font-size: 0.85em; white-space: nowrap; margin-top: 0.25em; }
.desc { background: var(--card); border-radius: 6px; padding: 0.3em 0.85em; flex: 1; line-height: 1.55; }
</style>

Tres partes a personalizar — el loop del agente no cambia:

<div class="parts">
<div class="part">
  <div class="tag">system_prompt</div>
  <div class="desc">Define el rol y el tono del agente. Escribe aquí qué hace tu startup, qué puede y qué no puede hacer el asistente.</div>
</div>
<div class="part">
  <div class="tag">tools</div>
  <div class="desc">Lista de herramientas disponibles. Cada una necesita nombre, descripción y esquema de parámetros. Empieza con 1–2 tools y añade más cuando las necesites.</div>
</div>
<div class="part">
  <div class="tag">ejecutar_tool</div>
  <div class="desc">El dispatcher que conecta Claude con tus datos reales. Sustituye los datos simulados por consultas a tu BD o llamadas a tu API.</div>
</div>
</div>

<p style="font-size:0.65em;color:#7a7890;margin-top:auto">▶ <a href="https://github.com/ssoto/applied-ai/blob/main/sdk_examples/04_template.py" target="_blank" style="color:inherit">sdk_examples/04_template.py</a></p>

---

<!-- _class: lead -->

# Q&A

---

<!-- _class: lead -->

# ¡Gracias! 🙌

Ha sido un placer aprender juntos

<br>

**¿Nos dejas tu feedback?**

![w:180](assets/qr_feedback.png)

<small style="font-size:0.55em;color:#7a7890">https://forms.gle/2eLq7PucCT66i7aF6</small>

[← Volver al índice](index.html)
