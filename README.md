# giovapagano.github.io

Personal academic website **and** PDF CV, both generated from the same data.

## Where to edit

Everything you normally touch is in **`_data/cv/`**:

| File | What it holds | Shows up in |
|---|---|---|
| `profile.yml` | name, position, affiliation, email, photo, social links | sidebar, PDF header |
| `sections.yml` | order and titles of CV sections | PDF, `/cv/`, `/publications/` |
| `appointments.yml` | positions (`current: true` for ongoing ones) | PDF, `/cv/` |
| `education.yml` | degrees | PDF, `/cv/` |
| `publications.bib` | all papers (see below) | PDF, `/cv/`, `/publications/`, `/research/`, home |
| `teaching.yml` | courses and workshops taught | PDF, `/cv/`, `/teaching/` |
| `talks.yml` | workshops and invited seminars | PDF, `/cv/` |
| `conferences.yml`, `service.yml`, `languages.yml`, `skills.yml` | the remaining CV sections | PDF, `/cv/` |

Outside `_data/cv/`:

- `index.md`: the bio on the home page
- `_data/research.yml`: research projects (title, image, summary)

Push to `main` and the workflow in `.github/workflows/deploy.yml` rebuilds the
PDF (`/files/Giovanni_Pagano_CV.pdf`) and the site together.

### Entries

Dated entries use `when`, `title` and optional `details`:

```yaml
- when: Dec 2025–Present
  current: true
  title: Research Fellow, Department of Social and Political Sciences, University of Milan
  details: "Scientific supervisor: Prof. Luigi Curini."
```

- Text accepts light markdown: `*italic*`, `**bold**`, `[link](https://…)`.
  Special LaTeX characters (`&`, `%`, `_` …) are escaped for you.
- Wrap a value in double quotes if it contains `: ` (colon + space).
- Add `web: false` or `pdf: false` to an entry (or a section in `sections.yml`)
  to keep it out of one of the two outputs.

### Publications

`publications.bib` is ordinary BibTeX, printed by biblatex in the PDF. The
`keywords` field decides the section: `peerreviewed`, `bookchapter`,
`workingpaper` or `wip`. Optional fields used only by the website:

```bibtex
  abstract = {...},             % collapsible abstract
  project  = {eu-laws},         % attaches the paper to a project in _data/research.yml
  url      = {https://...},     % link (not printed in the PDF)
  pdf      = {/files/paper.pdf},% local copy
```

A `doi` is printed in the PDF and linked on the website.

## Layout of the repository

```
_data/cv/          content (see above)
_data/research.yml research projects
cv/main.tex        PDF template (preamble and styling)
cv/build.py        turns _data/cv into cv/generated/*.tex and _data/publications.json
_layouts/base.html, _includes/site/, assets/site.css   website theme
index.md, research.md, publications.md, teaching.md, cv.md   pages
```

## Preview locally

```bash
pip install pyyaml
python3 cv/build.py                  # regenerate from _data/cv
cd cv && latexmk -lualatex main.tex  # PDF (needs TeX Live + biber)
cd .. && bundle install && bundle exec jekyll serve
```
