---
layout: base
title: Publications
permalink: /publications/
redirect_from:
  - /publication/2026-01-01-Identifying-delegation-and-constraints-in-legislative-texts-A-computational-method-applied-to-the-European-Union
  - /publication/2026-identifying_delegation_and_constraints.md
  - /publication/2026-06-01-The-gender-gap-in-language-emotionality-a-focus-on-the-Italian-parliament-1948-2020
  - /publication/Concepts-and-measures-of-bureaucratic-constraints-in-European-Union-laws-from-handcoding-to-machinelearning
  - /publication/Generational-gap-and-post-ideological-politics-in-Italy-POSTGEN-A-generation-aware-analysis-of-ideological-destructuring-and-political-change-in-the-Italian-case
  - /publication/Facebook-as-a-media-digest-user-engagement-and-party-references-to-hostile-and-friendly-media-during-an-election-campaign
  - /publication/Disinformation
  - /publication/Misinformation
  - /publication/The-2019-EP-Election-in-Italy-A-Titanic-Victory-for-Salvinis-League
  - /publication/2025-democratic-rhetoric-transitions
  - /publication/2025-work-in-progress-visual-consistency
  - /publication/2025-working-paper-empowerment-commission
---

{%- assign sections = site.data.cv.sections | where: "style", "publications" | where_exp: "s", "s.web != false" %}
{%- for sec in sections %}
{% include site/cv-section.html section=sec %}
{%- endfor %}
