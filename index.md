---
layout: base
title: About
hide_title: true
permalink: /
redirect_from:
  - /about/
  - /about.html
---

I am a Research Fellow in the [Department of Social and Political Sciences](https://sps.unimi.it/) at the University of Milan, where I work with Luigi Curini. I bring computational methods for text, images and legal documents to long-standing questions in comparative politics. My main research concerns multimodal political communication: how parties and leaders combine words and images in fragmented media environments, and what these strategies mean for political competition and democratic representation.

My other projects fall into two strands. The first concerns executive power in the European Union. With Fabio Franchino and Marta Migliorati, I measure delegation and constraint across more than 9,000 EU laws adopted since 1958, to explain why the European Commission's powers keep growing and how much flexibility member states retain. With Alessia Damonte, I am extending this approach to Italian legislation to detect the political capture of bureaucracies under democratic backsliding. The second strand concerns the pressures on democratic politics: how leaders of autocratizing regimes appropriate the language of democracy, how radical right candidates mobilize citizens around visions of the past and the future, how gendered expectations shape the tone of parliamentary speech, and how younger generations form political attitudes as traditional ideologies lose their hold.

Before my current position, I was a postdoctoral researcher on [*VIPoP — The Visual Politics of Populism*](https://x.com/vipop_project) (PRIN, 2023–2025) and in the DAPS&CO programme, and I completed my PhD at [NASP](https://www.nasp.eu/training/phd-programmes/pols.html) in 2022 with a dissertation on the 2019 European Parliament election campaign on Twitter. On this site you can find my [research projects](/research/), [publications](/publications/), [teaching](/teaching/) and [CV](/cv/).

<section class="home-block">
  <h2>Recent publications</h2>
  {%- assign recent = site.data.publications | where_exp: "p", "p.keyword contains 'peerreviewed'" %}
  <ol class="pubs">{% for pub in recent limit: 3 %}{% include site/pub.html pub=pub compact=true %}{% endfor %}</ol>
  <p><a class="more" href="{{ '/publications/' | relative_url }}">All publications →</a></p>
</section>
