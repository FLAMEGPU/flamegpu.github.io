---
title: "FLAME GPU 2 Case Studies"
---

FLAME GPU has been used within a wide range of industrial and research applications. Some examples are presented below.

<!-- Completely custom html / css, because undoing feature-row is a lot of effort.  -->
<div class="flex_feature_container small-2-col medium-3-col">
  {% for m in site.data.models %}
    <div class="flex_feature_item">
      <div class="flex_feature_item_teaser">
        {% if m.image_url %}
          <a href= "{{ m.more_url }}"><img src="{{ m.image_url | relative_url }}" alt="Image of {{ m.name }} Model in FLAME GPU 2"></a>
        {% endif %}
      </div>
      <div class="flex_feature_item_body">
        <h3><a href="{{ m.more_url }}">{{ m.name }}</a></h3>
        <div class="">
          {{ m.description | markdownify }}
        </div>
      </div>
    </div>
  {% endfor %}
</div>
