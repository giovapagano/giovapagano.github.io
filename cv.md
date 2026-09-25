---
layout: base
title: Curriculum Vitae
permalink: /cv/
redirect_from:
  - /resume
---

<p class="cv-download"><a class="button" href="{{ site.cv_pdf | relative_url }}?v={{ site.time | date: '%s' }}"><i class="fa-solid fa-file-arrow-down"></i> Download PDF</a></p>

{%- for sec in site.data.cv.sections %}
  {%- if sec.web == false %}{% continue %}{% endif %}
  {% include site/cv-section.html section=sec compact=true %}
{%- endfor %}
