---
layout: base
title: About
hide_title: true
permalink: /
redirect_from:
  - /about/
  - /about.html
---

I am a political scientist and Research Fellow in the [Department of Social and Political Sciences](https://sps.unimi.it/) at the University of Milan, where I work with Luigi Curini. I hold a PhD in Political Studies from [NASP](https://www.nasp.eu/training/phd-programmes/pols.html) (University of Milan, 2022). My research sits at the intersection of comparative politics, political communication, and computational social science. My main research concerns multimodal political communication: how parties and leaders combine words and images in fragmented media environments, and what these strategies mean for political competition and democratic representation.

My other projects fall into two strands. The first concerns executive power in the European Union. With Fabio Franchino and Marta Migliorati, I measure delegation and constraint across more than 9,000 EU laws adopted since 1958, to explain why the European Commission's powers keep growing and how much flexibility member states retain. With Alessia Damonte, I am extending this approach to Italian legislation to detect the political capture of bureaucracies under democratic backsliding.

The second strand concerns the pressures on democratic politics: how leaders of autocratizing regimes appropriate the language of democracy, how radical right candidates mobilize citizens around visions of the past and the future, and how gendered expectations shape the tone of parliamentary speech.

Before my current position, I was a postdoctoral researcher on [*VIPoP — The Visual Politics of Populism*](https://x.com/vipop_project) (PRIN, 2023–2025) and in the DAPS&CO programme. My doctoral dissertation examined political communication during the 2019 European Parliament election campaign on Twitter.

On this site you can find my [research projects](/research/), [publications](/publications/), [teaching](/teaching/) and [CV](/cv/).

<section class="home-block">
  <h2>Recent publications</h2>
  {%- assign recent = site.data.publications | where_exp: "p", "p.keyword contains 'peerreviewed'" %}
  <ol class="pubs">{% for pub in recent limit: 3 %}{% include site/pub.html pub=pub compact=true %}{% endfor %}</ol>
  <p><a class="more" href="{{ '/publications/' | relative_url }}">All publications →</a></p>
</section>
