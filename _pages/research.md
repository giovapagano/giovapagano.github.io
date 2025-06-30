---
layout: archive
title: "Research"
permalink: /research/
author_profile: true
---

{% include base_path %}

{% assign journals = site.research | where: "category", "journal" %}
{% assign bookchapters = site.research | where: "category", "bookchapter" %}
{% assign books = site.research | where: "category", "book" %}
{% assign workingpapers = site.research | where: "category", "workingpaper" %}
{% assign workinprogress = site.research | where: "category", "workinprogress" %}
{% assign others = site.research | where: "category", "other" %}
{% assign uncategorized = site.research | where_exp: "post", "post.category == nil" %}

{% if journals.size > 0 %}
<h2>Journal Articles</h2>
<hr />
<ul>
  {% for post in journals reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}
</ul>
{% endif %}

{% if bookchapters.size > 0 %}
<h2>Book Chapters</h2>
<hr />
<ul>
  {% for post in bookchapters reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}
</ul>
{% endif %}

{% if books.size > 0 %}
<h2>Books</h2>
<hr />
<ul>
  {% for post in books reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}
</ul>
{% endif %}

{% if workingpapers.size > 0 %}
<h2>Working Papers</h2>
<hr />
<ul>
  {% for post in workingpapers reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}
</ul>
{% endif %}

{% if workinprogress.size > 0 %}
<h2>Work in Progress</h2>
<hr />
<ul>
  {% for post in workinprogress reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}
</ul>
{% endif %}

{% assign safe_others = others %}
{% if safe_others == nil %}
  {% assign safe_others = "" | split: "" %}
{% endif %}

{% assign safe_uncategorized = uncategorized %}
{% if safe_uncategorized == nil %}
  {% assign safe_uncategorized = "" | split: "" %}
{% endif %}

{% assign combined_other = safe_others | concat: safe_uncategorized %}
