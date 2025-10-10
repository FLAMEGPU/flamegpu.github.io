---
title: "FLAME GPU 2 Models"
permalink: "models/benchmarking"
---

FLAME GPU 2 models can be contained in their own source code repositories. 
This page provides a selection of models implemented in FLAME GPU 2, which can be built following the instructions provided with each repository.

If you would like to contribute your own model to this page you should use the FLAME GPU 2 example template and then [contact us](../contact) to include your model.

FLAME GPU 1.x models are included with the FLAME GPU 1.x SDK, which can be found via the  [download](../download) page.

<!-- Compeltely custom html / css, because undoing feature-row is a lot of effort.  -->
<div class="flex_feature_container small-2-col medium-3-col">
  {% for m in site.data.benchmarks %}
    <div class="flex_feature_item">
      <div class="flex_feature_item_teaser">
        {% if m.image_url %}
          <img src="{{ m.image_url | relative_url }}" alt="Image of {{ m.name }} Model in FLAME GPU 2">
        {% else %}
          {% if m.language == "Python" %}
            <img src="{{ 'assets/images/pyfgpu2_icon_512.png' | relative_url }}" alt="Default Python model image in FLAME GPU 2">
          {% else %}
            <img src="{{ 'assets/images/fgpu2_icon_512.png' | relative_url }}" alt="Default C++ model image in FLAME GPU 2">
          {% endif %}
        {% endif %}
      </div>
      <div class="flex_feature_item_body">
        <h3>{{ m.name }}</h3>
        <div class="">
          {{ m.description | markdownify }}
        </div>
      </div>
      <div class="flex_feature_item_footer">
        {% if m.github_url %}
          <a href="{{ m.github_url }}" class="btn btn--primary">GitHub</a>
        {% endif %}
      </div>
    </div>
  {% endfor %}
</div>
