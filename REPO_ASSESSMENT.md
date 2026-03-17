# Repository Assessment

## Executive summary
This repository is a customized **Academic Pages** (Jekyll) academic website for `giovapagano.github.io`.
It is structurally healthy and content-rich, with clear separation between content collections (`_publications`, `_teaching`, `_research`, `_talks`) and presentation layers (`_layouts`, `_includes`, `_sass`, `assets`).

Overall assessment: **Good foundation, moderate maintenance risk**, mainly due to aging toolchain conventions and limited automated validation.

---

## What is working well

- Clear Jekyll content model with collections for research, teaching, talks, and publications.
- Site metadata and author profile are configured and populated in `_config.yml`.
- Supporting scripts exist for CV generation and publication/talk markdown generation (`scripts/`, `markdown_generator/`).
- Docker-based local workflow is present (`Dockerfile`, `docker-compose.yaml`) for reproducible local builds.

---

## Key risks and gaps

### 1) Dependency/tooling age and drift
- `package.json` advertises a very permissive and outdated Node engine floor (`>= 0.10.0`), which no longer reflects real-world supported runtimes.
- Mixed Ruby/Jekyll dependency strategy (`github-pages` + explicit plugin gems) increases risk of version conflicts over time.

### 2) Automation is limited and partially stale
- There is one workflow (`scrape_talks.yml`), but no CI check for site build/lint on pull requests.
- Workflow uses older action major versions (`actions/checkout@v2`, `actions/setup-python@v2`) and broad `git add .` commit behavior.

### 3) Content-generation scripts have known technical debt
- Multiple `TODO`s in `markdown_generator/*` indicate unaddressed parser and format limitations.
- Notebook-driven generation can be brittle in CI compared to script-only pipelines.

### 4) Config hygiene issues
- `_config.yml` still references upstream template repository (`academicpages/academicpages.github.io`) instead of the deployed fork.
- `analytics.provider` is set to the string `"false"`, which can be semantically confusing versus boolean false.

---

## Recommendations (prioritized)

### High priority (stability)
1. Add a CI workflow that runs Jekyll build on push/PR.
2. Update GitHub Actions to current major versions and narrow commit scope in automation.
3. Normalize `_config.yml` values (`repository`, booleans) to avoid subtle behavior issues.

### Medium priority (maintainability)
4. Document a single blessed local build path (`bundle exec jekyll serve` or Docker) with exact versions.
5. Review Ruby gem constraints to minimize conflicts with `github-pages`.
6. Convert notebook automation to deterministic Python scripts where practical.
7. Design a bibliography-driven content pipeline so the backbone section markdown files are automatically reconciled from a master `.bib` file: existing `.md` entries should be updated, missing ones created, and obsolete ones removed based on publication status.

### Specific idea to develop
- Introduce a **single source of truth**: a master `.bib` file maintained in the CV repository and pushed/synced into this site repository.
- Build a sync step that reads the master `.bib` and publication status metadata, then:
  - updates matching records under `/_publications` (and other relevant section folders),
  - creates new markdown files for new bibliography entries,
  - removes markdown files for deprecated/withdrawn entries when status requires it.
- Ensure this process is idempotent and safe (dry-run mode + change summary) so it can run in CI or as a scheduled/manual maintenance task.

### Low priority (quality improvements)
8. Add basic content linting (front matter + link checks).
9. Address `markdown_generator` TODOs or document unsupported edge cases clearly.

---

## Suggested next milestone
A practical next milestone is a **"Build reliability" PR** that:
- adds PR build checks,
- modernizes workflow actions,
- and performs a small config hygiene cleanup.

This should materially reduce breakage risk without changing site content.
