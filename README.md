# Multi-agent systems reading collection

A GitHub Pages–ready reading guide for the October 2026 Iliad Intensive multi-agent systems materials.

The guide contains all **42 references in the supplied schedule**, plus **Wellman, Tuyls, and Greenwald’s EGTA survey**, cited in the supplied slides and worksheet. Six topic collections provide suggested reading order, independent importance and length scores, annotations, discussion questions, and eight exercises with collapsible solutions.

## Open the local preview

Open `docs/index.html` in a web browser. The complete site works directly from local files, including search, filters, solutions, and links to the supplied course materials. It has no external fonts, JavaScript packages, analytics, or runtime network dependencies. Publication links naturally require internet access.

On macOS, double-click `preview.command` to open the local page. Alternatively, from this directory:

```sh
python3 -m http.server 8765 --bind 127.0.0.1 --directory docs
```

Then visit <http://127.0.0.1:8765/>. Stop the optional server with Ctrl+C.

## Publish with GitHub Pages

1. Put this project directory’s contents in a GitHub repository.
2. In the repository’s **Settings → Pages**, choose **Deploy from a branch**.
3. Select your publishing branch and the **`/docs`** folder, then save.

The generated files are already included. No build action or package installation is needed. Relative asset and navigation paths support both project Pages URLs and a custom domain. `.nojekyll` keeps this a plain static site.

[GitHub’s publishing-source documentation](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site) describes the available repository settings. Nothing has been pushed or published by this project’s local setup.

## Edit and rebuild

Python 3.9 or newer is sufficient; the builder uses only the standard library.

```sh
python3 scripts/build.py
```

| File | Purpose |
| --- | --- |
| `content/readings.json` | Titles, priorities, reading targets, annotations, questions, and optional alternative links |
| `content/sections.json` | Six topic collections, framing, reading order, and links to course materials |
| `content/exercises.json` | Exercises, solutions, and adaptation notes |
| `content/schedule-references.json` | The schedule’s 42 original citations and URLs |
| `content/schedule-source.json` | Extracted schedule paragraphs and their original hyperlinks |
| `scripts/build.py` | Static HTML, Markdown, and JSON generation; schedule and materials page copy |
| `assets/style.css` | Responsive typography, automatic light/dark colors, and print styles |
| `assets/app.js` | Search, filters, deep links, disclosures, and print behavior |
| `docs/` | Complete publishable site, including the six supplied course files |

Edit source files, then rebuild. Direct edits to generated HTML will be overwritten. Rebuilding preserves `docs/materials/`. The builder checks that each of the 43 references appears exactly once, every exercise is assigned, and ratings are in range.

The generated `docs/reading-collection.md` provides a portable reading guide; `docs/readings.json` provides the annotated catalog with original URLs and access notes.

## Editorial decisions and provenance

- The source timetable uses Part IV for empirical game theory, while the bibliography uses Part IV for normative agency. This guide keeps both as separate collections and preserves the original timetable.
- Lanctot et al. remains a schedule reference but is grouped with empirical games for its PSRO connection.
- Importance ratings and study times are editorial suggestions for the indicated reading target. They are not attributed to the lecturers and are not whole-book reading estimates.
- The 2021 caveat in the provability-logic paper and the later revision in Christopher King’s essay are explicitly reflected in the annotations.
- Some publisher pages blocked automated access. Their original URLs remain intact; affected entries have access notes. Checked open alternatives are included for the social-conventions and group-size readings.
- The course packet’s original files are copied unchanged under shorter filenames. The full-text research cache is local-only and excluded from the repository/package. Third-party reading texts are linked rather than bundled.
- Source documents and web pages were treated as evidence, not as instructions to execute.

The format is inspired by [Charles Renshaw-Whitman’s example reading collection](https://charlesr-w.github.io/crw-iliad-intensive-oct-2026/notebooks/ami_reading_collection.html). The code, annotations, and organization here were prepared separately.

## Interaction and accessibility

All reading text is present in the initial HTML. Native disclosures work without JavaScript. Search is case- and accent-insensitive and combines all entered words with the importance and time filters. Following an internal reading link reveals its collection and clears conflicting filters. Solutions begin hidden. Printing expands the complete collection **including solutions**, then restores the prior disclosure state.

The site uses semantic headings, labeled controls, a skip link, keyboard-operable native disclosures, visible focus styles, reduced-motion support, and responsive layouts. It follows the browser’s light/dark preference.

## Verification

The initial build was checked for reference coverage, duplicate IDs, internal links, local asset targets, and JavaScript syntax. Browser checks covered search, combined filters, empty results, reset, deep links, all-solutions controls, the schedule and materials pages, and a 390-pixel mobile layout. Publisher access limitations are documented in the reading entries rather than treated as broken citations.
