---
layout: base
title: About
hide_title: true
permalink: /
redirect_from:
  - /about/
  - /about.html
---

<p class="lede">Research Fellow in political science at the University of Milan, working on multimodal political communication and computational methods.</p>

Since December 2025, I am a Research Fellow in the [Department of Social and Political Sciences](https://sps.unimi.it/) at the University of Milan. I study multimodal political communication in fragmented media environments, leveraging large-scale datasets and advanced computational methods to analyse how political actors strategically combine text and visuals. My work examines the implications of these strategies for political competition and democratic representation in the digital age.

From 2023 to 2025, I was a Postdoctoral Research Fellow at the University of Milan, contributing to the [*VIPoP — The Visual Politics of Populism*](https://x.com/vipop_project) (PRIN 2023–2025) project, where I examined the strategic use of visual and textual communication by parties and leaders.

Before this position, I was a postdoctoral researcher in the [DAPs&CO program](https://www.unimi.it/en/ugov/ou-structure/department-social-and-political-sciences) on computational methods for political science, and completed my PhD at [NASP](https://www.nasp.eu/training/phd-programmes/pols.html), where I studied online campaigning and affective polarization during the 2019 European Parliament elections.

Across my research, I combine theory-driven political analysis with computational methods to examine how political actors communicate, govern, and compete — from multimodal campaign strategies and media narratives to legislative bargaining and executive discretion — and how these dynamics shape democratic representation.

<section class="home-block">
  <h2>Recent publications</h2>
  {%- assign recent = site.data.publications | where_exp: "p", "p.keyword contains 'peerreviewed'" %}
  <ol class="pubs">{% for pub in recent limit: 3 %}{% include site/pub.html pub=pub compact=true %}{% endfor %}</ol>
  <p><a class="more" href="{{ '/publications/' | relative_url }}">All publications →</a></p>
</section>
