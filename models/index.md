---
title: "FLAME GPU 2 Models"
---

FLAME GPU 2 models can be contained in their own source code repositories. 
This page provides a selection of models implemented in FLAME GPU 2, which can be built following the instructions provided with each repository.

If you would like to contribute your own model to this page you should use the FLAME GPU 2 example template and then [contact us](../contact) to include your model.


<!-- modified feature_row include -->
<div class="feature__wrapper">
  {% for m in site.data.models %}
    <div class="feature__item">
      <div class="archive__item">
        <div class="archive__item-teaser">
          {% if m.image_url %}
            <img src="{{ m.image_url | relative_url }}" alt="Image of {{ m.name }} Model in FLAME GPU 2">
          {% else %}
            {% if m.language == "Python" %}
              <img src="{{ 'assets/images/pyfgpu2_icon_512.png' | relative_url }}" alt="Default Python model image in FLAME GPU">
            {% else %}
              <img src="{{ 'assets/images/fgpu2_icon_512.png' | relative_url }}" alt="Default C++ model image in FLAME GPU">
            {% endif %}
          {% endif %}
        </div>
          <div class="archive__item-body">
            <h3 class="archive__item-title">{{ m.name }}</h3>
            <div class="archive__item-excerpt">
              {{ m.description | markdownify }}
            </div>
            {% if m.github_url %}
              <p><a href="{{ m.github_url }}" class="btn btn--primary">GitHub</a></p>
            {% endif %}
        </div>
      </div>
    </div>
  {% endfor %}
</div>

FLAME GPU 1.x models are included with the FLAME GPU 1.x SDK, which can be found via the  [download](../download) page.
