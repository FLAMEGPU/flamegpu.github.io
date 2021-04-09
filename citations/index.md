---
title: "Articles using or citing FLAME GPU"
---

The following {{ site.data.citations.size }} citations reference one of the [FLAME GPU publications](/publications/).

{% assign i = 0 %}
{% for publication in site.data.citations %}
 {{i}}. *{{publication.bib.author}}*, [**{{publication.bib.title}}**]({{publication.pub_url}}) {% if publication.bib.pub_type == 'article' %} {{publication.bib.journal}} ({{publication.bib.pub_year}}) {% if publication.bib.volume %}Vol {{publication.bib.volume}}{% endif %} {% if publication.bib.pages %}Pages {{publication.bib.pages}}.{% endif %} {% else %} {{publication.bib.booktitle}} ({{publication.bib.pub_year}}) {% endif %} - {{publication.num_citations}} Citations
{% assign i = i | plus:1 %}
{% endfor %}