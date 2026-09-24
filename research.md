---
layout: base
title: Research
permalink: /research/
---

{%- for project in site.data.research %}
<article class="project" id="{{ project.slug }}">
  {%- if project.image %}<img src="{{ project.image | relative_url }}" alt="" loading="lazy">{% endif %}
  <div class="project-body">
    <h2>{{ project.title }}</h2>
    <p>{{ project.summary }}</p>
    {%- assign linked = site.data.publications | where: "project", project.slug %}
    {%- if linked.size > 0 %}
    <h3>Related work</h3>
    <ol class="pubs">{% for pub in linked %}{% include site/pub.html pub=pub compact=true %}{% endfor %}</ol>
    {%- endif %}
  </div>
</article>
{%- endfor %}
