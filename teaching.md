---
layout: base
title: Teaching
permalink: /teaching/
redirect_from:
  - /teaching/2021-2026-political-science
  - /teaching/2023-2026-intro-r
  - /teaching/2023-data-management
  - /teaching/2023-multivariate-analysis
  - /talks/
---

<ul class="courses">
{%- for e in site.data.cv.teaching %}
  {%- if e.web == false %}{% continue %}{% endif %}
  <li class="course">
    <div class="course-head">
      <h2>{{ e.course }}</h2>
      <span class="years">{% if e.period %}{{ e.period }}{% else %}{{ e.years | sort | join: " · " }}{% endif %}</span>
    </div>
    <p class="course-meta">{% if e.role %}{{ e.role }} · {% endif %}{{ e.institution }}</p>
    {%- if e.details %}<p class="course-details">{{ e.details | markdownify | remove: "<p>" | remove: "</p>" | strip }}</p>{% endif %}
  </li>
{%- endfor %}
</ul>
