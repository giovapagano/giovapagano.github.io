---
layout: archive
title: "CV"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

You can download my [CV (here in PDF)](/files/Giovanni_Pagano_CV.pdf).


Current Appointments
======
* 2023–present: Post-Doctoral Research Fellow  
  * University of Milan  
  * Project: *VIPoP — The Visual Politics of Populism (PRIN 2023–2025)*  
  * Research focus: Computational methods for visual and textual political communication  


Past appointments
======

* 2022–2023: Postdoctoral Researcher  
  * DAPs&CO program, University of Milan  
  * Research and teaching on computational methods for political science  

* 2015-2019 Research Associate at REScEU \ EuVisions
  * External research associate at REScEU \ EuVisions (ERC-funded, University of Milan; PI: Prof. Maurizio Ferrera), Centro di Ricerca e Documentazione L. Einaudi.
  * Computational analysis of social media data  


Education
======
* Ph.D. in Political Science, [NASP](https://www.nasp.eu/training/phd-programmes/pols.html), University of Milan, 2022  
  * Dissertation on online campaigning and affective polarization during the 2019 European Parliament elections  

* M.A. in Political Studies and International Relations. University of Turin, 2012, (110/110 cum laude)


Publications
======
<ul>
{% for post in site.publications reversed %}
  {% unless post.category == "wip" or post.category == "workingpaper" %}
    {% include archive-single-cv.html %}
  {% endunless %}
{% endfor %}
</ul>


Talks
======
<ul>{% for post in site.talks reversed %}
  {% include archive-single-talk-cv.html %}
{% endfor %}</ul>


Teaching
======
<ul>{% for post in site.teaching reversed %}
  {% include archive-single-cv.html %}
{% endfor %}</ul>


Service and leadership
======
 * Thesis supervision, for students of the MA in Public and Corporate Communication (2022-2024). 


Skills
======
* Computational text analysis
* Computer vision for social science
* Statistical analysis (R, Python)
* Data management for social science
