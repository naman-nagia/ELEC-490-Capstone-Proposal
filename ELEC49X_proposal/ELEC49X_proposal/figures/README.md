# Figures

Put project diagrams and plots here. PDF works well for vector diagrams; PNG and JPEG are also supported by pdfLaTeX. Prefer filenames with letters, numbers, and hyphens.

Replace a `\FigurePlaceholder` command with:

```tex
\includegraphics[width=\linewidth,height=2.5in,keepaspectratio]{figures/system-diagram.pdf}
```

Keep the surrounding `figure`, `\caption`, and `\label` commands. Refer to the result with `Figure~\ref{fig:system}`. For an optional cover logo, set `\ProjectLogo` in `metadata.tex` to a file in this folder.
