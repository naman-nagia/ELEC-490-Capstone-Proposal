#!/usr/bin/env sh
set -eu
cd "$(dirname "$0")"
if command -v latexmk >/dev/null 2>&1; then
    latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error main.tex
else
    pdflatex -interaction=nonstopmode -halt-on-error -file-line-error main.tex
    pdflatex -interaction=nonstopmode -halt-on-error -file-line-error main.tex
    pdflatex -interaction=nonstopmode -halt-on-error -file-line-error main.tex
fi
