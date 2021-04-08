---
title: "FLAME GPU 2 Models"
---

FLAME GPU 2 example models can be downloaded individually from this page. Each model has a depdnendacy on the main FLAME GPU 2 codebase which will be cloned via cmake when you build the model. If you are looking for FLAME GPU 1 models then visit the [download](../download) page to download the FLAME GPU 1.X SDK (which includes packaged examples).

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
            <h2 class="archive__item-title">{{ m.name }}</h2>

            <div class="archive__item-excerpt">
              {{ m.description | markdownify }}
            </div>

            <p><a href="{{ m.download_url }}" class="btn btn--primary">Download</a></p>
        </div>
      </div>
    </div>
  {% endfor %}

</div>

If you would like to contribute your own model to this page you should use the FLAME GPU 2 example template and then [contact us](../contact) to include your model.
