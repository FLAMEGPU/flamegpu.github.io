---
title: "FLAMEGPU Publications"
---

The following is a list of publications which describe the FLAME GPU software or aspects of its design.

{% assign i = 0 %}
{% for publication in site.data.publications %}
 {{i}}. *{{publication.bib.author}}*, [**{{publication.bib.title}}**]({{publication.pub_url}}) {% if publication.bib.pub_type == 'article' %} {{publication.bib.journal}} ({{publication.bib.pub_year}}) {% if publication.bib.volume %}Vol {{publication.bib.volume}}{% endif %} {% if publication.bib.pages %}Pages {{publication.bib.pages}}.{% endif %} {% else %} {{publication.bib.booktitle}} ({{publication.bib.pub_year}}) {% endif %}
{% assign i = i | plus:1 %}
{% endfor %}