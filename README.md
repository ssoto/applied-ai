# Applied AI — Open Future Ceuta

Presentaciones y ejemplos de código del taller **Applied AI** impartido en Open Future Ceuta (11 junio 2026).

**[Ver presentaciones →](https://ssoto.github.io/applied-ai/)**

## Estructura del taller

| Bloque | Tema | Duración |
|--------|------|----------|
| [Bloque 0](bloque0.md) | Bienvenida y Contexto | 15 min |
| [Bloque 1](bloque1.md) | Prompt Engineering (zero-shot, few-shot, CoT) | 60 min |
| [Bloque 2](bloque2.md) | Claude Cowork / Code (flujos sin código y con código) | 60 min |
| [Bloque 3](bloque3.md) | Claude SDK (API, tool use, primer agente) + Q&A | 60 + 15 min |

## Ejemplos de código (`sdk_examples/`)

Scripts Python para la parte práctica del Bloque 3. Prerrequisitos:

```bash
pip install anthropic
export ANTHROPIC_API_KEY="sk-ant-..."
```

| Script | Contenido |
|--------|-----------|
| `01_primera_llamada.py` | Llamada básica a la API |
| `02_tool_definition.py` | Definición de herramientas |
| `021_tool_call.py` | Parsing y ejecución de tool calls |
| `03_fitcoach_agent.py` | Loop agéntico completo con herramientas |
| `04_template.py` | Plantilla en blanco para los asistentes |

## Desarrollo local

```bash
make           # compila todas las presentaciones (incremental)
make preview   # servidor con live-reload en http://localhost:8080
make watch     # recompila automáticamente al guardar cambios
make bloque1.html  # compila un solo bloque
```

Los `.html` son artefactos compilados — edita siempre los `.md`.

## Tecnología

- **[Marp](https://marp.app/)** — compilador de Markdown a presentaciones HTML
- **`theme.css`** — tema `applied-ai` compartido por todos los bloques
- **GitHub Pages** — alojamiento estático (`.nojekyll` deshabilita Jekyll)

## Autor

**Sergio Soto Núñez** — AI Engineer @ [Diverger.ai](https://diverger.ai)  
[linkedin.com/in/sergiosotonunez](https://linkedin.com/in/sergiosotonunez)
