# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

A **GitHub Pages site** that hosts Marp-compiled presentations for an Applied AI workshop. The source of truth is the `.md` files; the `.html` files are compiled artifacts that must be regenerated whenever a `.md` changes.

## Build with Make

```bash
make          # compile all changed presentations (incremental)
make bloque1.html   # compile a single block
make watch    # watch *.md and theme.css, recompile on change (requires chokidar-cli)
make preview  # live-reload server on http://localhost:8080
make clean    # remove all compiled .html files
```

The Makefile tracks `theme.css` as a dependency — changing the theme recompiles every presentation automatically. After compilation, a 🤖 favicon is injected into each HTML file via `sed`.

## Compile manually (without Make)

```bash
# Single file
npx @marp-team/marp-cli@latest <file>.md -o <file>.html --html --theme theme.css

# All presentations at once
for f in bloque0 bloque1 bloque2 bloque3; do
  npx @marp-team/marp-cli@latest $f.md -o $f.html --html --theme theme.css
done
```

## Preview locally

```bash
make preview
# or directly:
npx @marp-team/marp-cli@latest --server .
```

Opens a live-reload server. Marp also has a VS Code extension that renders slides inline.

## File layout

| File/Dir | Role |
|----------|------|
| `index.html` | Hand-written navigation page (not compiled from Markdown) |
| `theme.css` | Shared Marp theme (`applied-ai`) — single source of truth for slide styles |
| `bloque{0-3}.md` | Marp source for each workshop block |
| `bloque{0-3}.html` | Compiled artifacts — do not edit directly |
| `assets/` | Images and data files referenced by slides (CSVs, PNGs, zip archives) |
| `sdk_examples/` | Standalone Python SDK examples used in bloque3 hands-on section |
| `slides.md` | Original demo presentation (kept for reference) |
| `generate_qr.py` | Regenerates `assets/qr.png` — run with `pip install qrcode && python generate_qr.py` |
| `.nojekyll` | Disables Jekyll so GitHub Pages serves the raw HTML |

## Presentation structure

All `.md` files use the shared `theme: applied-ai` theme defined in `theme.css`. The CSS variables (`--bg`, `--fg`, `--accent`, `--accent-2`, `--card`, `--border`) live only in that file. When adding a new presentation, set `theme: applied-ai` in its frontmatter — no `style:` block needed.

Slides are separated by `---`. Use `<!-- _class: lead -->` on a slide for the centred title layout and `<!-- _paginate: false -->` to hide the page number. Use `<!-- _class: compact-code -->` on slides with dense code blocks to reduce font size.

## Workshop blocks

| File | Topic | Duration |
|------|-------|----------|
| `bloque0` | Bienvenida y Contexto | 15 min |
| `bloque1` | Prompt Engineering (zero-shot, few-shot, CoT) | 60 min |
| `bloque2` | Claude Cowork / Code (no-code and code flows) | 60 min |
| `bloque3` | Claude SDK (API, tool use, first agent) + Q&A | 60 + 15 min |

## SDK examples (`sdk_examples/`)

Python scripts for the bloque3 hands-on section. Require `pip install anthropic` and `ANTHROPIC_API_KEY` set in the environment.

| File | What it demonstrates |
|------|----------------------|
| `01_primera_llamada.py` | Minimal `client.messages.create` call |
| `02_tool_definition.py` | Defining tools with `input_schema` |
| `021_tool_call.py` | Parsing and executing a tool call from the response |
| `03_fitcoach_agent.py` | Full agentic loop: tool use + multi-turn messages |
| `04_template.py` | Blank starting point for workshop participants |

The data files in `assets/` (`costes_q3_2024.csv`, `resenas_flowdesk.csv`, `analisis_margenes_q2_2024.md`) are sample datasets used as context in bloque2 and bloque3 exercises.
