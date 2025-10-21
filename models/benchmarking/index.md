---
title: "FLAME GPU 2 Models"
---

In order to evaluate the performance of FLAME GPU a number of benchmarking models exist which evaluate different scaling aspects of FLAME GPUs features. 

<!-- Completely custom html / css, because undoing feature-row is a lot of effort.  -->
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
