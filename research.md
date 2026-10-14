---
layout: base
title: Research
permalink: /research/
---

{%- for project in site.data.research %}
<article class="project" id="{{ project.slug }}">
  <div class="project-body">
    <h2>{{ project.title }}</h2>
    {%- if project.image %}
    <figure>
      <img src="{{ project.image | relative_url }}" alt="{{ project.caption | default: project.title | markdownify | strip_html | strip }}" loading="lazy">
      {%- if project.caption %}<figcaption>{{ project.caption | markdownify | remove: "<p>" | remove: "</p>" | strip }}</figcaption>{% endif %}
    </figure>
    {%- endif %}
    {{ project.summary | markdownify }}
    {%- if project.links %}
    <p class="project-links">{% for l in project.links %}<a class="chip" href="{{ l.url }}">{{ l.label }}</a>{% endfor %}</p>
    {%- endif %}
    {%- assign linked = site.data.publications | where: "project", project.slug %}
    {%- if linked.size > 0 %}
    <h3>Related work</h3>
    <ol class="pubs">{% for pub in linked %}{% include site/pub.html pub=pub compact=true %}{% endfor %}</ol>
    {%- endif %}
  </div>
</article>
{%- endfor %}
