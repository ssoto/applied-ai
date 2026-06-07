MARP    := npx @marp-team/marp-cli@latest
THEME   := theme.css
FLAGS   := --html --theme $(THEME)
BLOCKS  := bloque0 bloque1 bloque2 bloque3
SRCS    := $(addsuffix .md,  $(BLOCKS))
TARGETS := $(addsuffix .html, $(BLOCKS))

.PHONY: all watch preview clean help

help:
	@echo ""
	@echo "  Applied AI Workshop — targets disponibles"
	@echo ""
	@echo "  make all              Compila todas las presentaciones (incremental)"
	@echo "  make bloque0.html     Compila un bloque concreto"
	@echo "  make watch            Vigila cambios en .md y theme.css y recompila"
	@echo "  make preview          Servidor con live-reload en http://localhost:8080"
	@echo "  make clean            Elimina todos los HTML compilados"
	@echo "  make help             Muestra esta ayuda"
	@echo ""

all: $(TARGETS)

%.html: %.md $(THEME)
	$(MARP) $(FLAGS) $< -o $@
	@sed -i '' 's|</head>|<link rel="icon" href="data:image/svg+xml,<svg xmlns='"'"'http://www.w3.org/2000/svg'"'"' viewBox='"'"'0 0 100 100'"'"'><text y='"'"'.9em'"'"' font-size='"'"'90'"'"'>🤖</text></svg>"></head>|' $@

watch:
	@echo "Watching *.md y $(THEME) — Ctrl-C para salir"
	npx chokidar-cli "*.md" "$(THEME)" -c "make all"

preview:
	$(MARP) --server .

clean:
	rm -f $(TARGETS)
