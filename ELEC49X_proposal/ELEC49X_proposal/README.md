# ELEC 490/498 proposal LaTeX template
The latex for this template was created using AI, but we've checked and edited it! :)

It can be used as a guide for your proposal. Feel free to edit any fields as desired, but stick to the formatting described below.


For an optional schedule reference, use `Appendix~\ref{app:schedule}` and enable the appendices. The label `ProposalBodyEnd` marks the last body page for page-count checks.


## Start here

1. Open `main.tex` as the root document and select pdfLaTeX.
2. Edit `metadata.tex` for the project title, group, members, supervisor, date, version, and academic year.
3. Replace each entire `\TemplateField{...}` command in `sections/` with project-specific text. Make sure to replace the command together with its braces so that your text is appropriately colored. Apply the same replacement to the fields in `metadata.tex`. The blue `\Guideline{}` text provides you with some suggestions as to what to write in each section.
4. Put diagrams in `figures/` and replace `\FigurePlaceholder` with `\includegraphics`. There is a working example in the README in that folder.
5. Update the bibliography entries in the references section and cite them with `\cite{key}`.
6. Change `\showguidancetrue` to `\showguidancefalse` in `metadata.tex` for the submission version. This switch hides writing guidance; bracketed fields remain visible until replaced.
7. Compile and review the PDF, page count, tables, citations, and remaining fields.

## Structure

| File or folder | Purpose |
| --- | --- |
| `main.tex` | Assembles the document with `\input`. |
| `metadata.tex` | Central project details and template switches. |
| `preamble.tex` | Fonts, colours, layout, headers, tables, and reusable commands. |
| `sections/` | Separate numbered `.tex` files for the document sections. |
| `figures/` | Project diagrams, plots, and an optional logo. |
| `build.sh`, `Makefile` | Local build commands. |
| `main.pdf` | Compiled doc. |

## Compile

If you use `vs code`, you can configure your latex compiler to compile on save. The output is `main.pdf`. You can rename your pdf as you wish.

Otherwise, ChatGPT told me that you can build:

With TeX Live or MiKTeX and the standard packages used in `preamble.tex`:

```sh
./build.sh
```

Alternative:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

The bibliography uses `thebibliography` in a separate file within the `sections` directory, and numbers your `\cite{...}` references.

For Overleaf (which is useful for real-time collaboration with your groupmates), upload the ZIP as a new project, select `main.tex` as the main document, and use pdfLaTeX.

## Formatting and optional content

- Letter paper, 1-inch margins, 12-point font, and 1.5-spaced body text.
- Tables can be 12-point text and single-spaced cells. The contents and cover also use single spacing.
- The cover page contains project and team information. Front matter is numbered with Roman numerals, and the main body starts at page 1, which continues to the last page of the document, even though the references and appendices are not included in the 8-page limit.
- `\includeappendicestrue` includes the appendix file; `\includeappendicesfalse` omits it.
- `\includeindustrypartnertrue` displays the industry partner on the cover. Set the partner name in `metadata.tex`.
- Set `\ProjectLogo` to an image path to display an optional project logo.
- Each major section starts on a new page, but you can remove that by deleting `\clearpage` to shorten the page count.
- Requirement, test, milestone, and work-package IDs are editable placeholders for traceability.
- `\jj` produces the imaginary unit j in mathematics, for example `$Z=R+\jj X$`.

## Before submission

Replace every `\TemplateField{...}`, including the cover, tables, captions, and bibliography. Replace placeholder figures and tables.