---
title: ""
layout: splash
header:
  overlay_particles: true
  actions:
    - label: "Download"
      url: "/download/"
    - label: "GitHub"
      url: "https://github.com/FLAMEGPU/FLAMEGPU2/"
    - label: "Docs"
      url: "https://docs.flamegpu.com"
     - label: "Try on Colab"
       url: "https://colab.research.google.com/github/FLAMEGPU/FLAMEGPU2-tutorial-python/blob/google-colab/FLAME_GPU_2_python_tutorial.ipynb"
excerpt: "The Flexible Large-scale Agent Modelling Environment for the Graphics Processing Unit (GPU)"
feature_row:
  - image_path: /assets/images/gpu_birds_square.png
    alt: "About FLAME GPU"
    title: "About FLAME GPU"
    excerpt: "Find out about FLAME GPU 2 and its new features including a recorded presentation and links to publications and citations."
    url: "/about/"
    btn_class: "btn--primary"
    btn_label: "Learn more"
  - image_path: /assets/images/models_square.png
    alt: "FLAME GPU models"
    title: "Explore the examples"
    excerpt: "Browse the model database for example models which highlight key features or demonstrate performance. Download them and try them for yourself."
    url: "/models/"
    btn_class: "btn--primary"
    btn_label: "Learn more" 
  - image_path: /assets/images/github_square.png
    alt: "Github"
    title: "Explore the Source"
    excerpt: "Go to GitHub to browse the source code of the simulator, docs and this website."
    url: "https://github.com/FLAMEGPU/"
    btn_class: "btn--primary"
    btn_label: "Goto GitHub"   	
---

![FLAME GPU 2 logo]({{ "/assets/images/fgpu2_icon_256.png" | relative_url }}){: .align-right}

FLAME GPU is a GPU accelerated simulator for domain independent complex systems simulations.
Version 2 brings a complete re-write of the existing library offering greater flexibility, an improved interface for agent scripting, CUDA C++ & python3  interfaces and better research software engineering.

FLAME GPU provides a mapping between a formal agent specifications with C based scripting and optimised CUDA code.
This includes a number of key ABM building blocks such as multiple agent types, agent communication and birth and death allocation.

The advantages of our contribution are three fold.

+ Firstly Agent Based (AB) modellers are able to focus on specifying agent behaviour and run simulations without explicit understanding of CUDA programming or GPU optimisation strategies.

+ Secondly simulation performance is significantly increased in comparison with desktop CPU alternatives.
This allows simulation of far larger model sizes with high performance at a fraction of the cost of grid based alternatives.
+ Finally massive agent populations can be visualised in real time as agent data is already located on the GPU hardware.

<!-- {% include feature_row %} -->
<!-- Custom feature row implementation for flexbox. -->

<div class="flex_feature_container">
  {% for f in feature_row %}
    <div class="flex_feature_item">
      {% if f.image_path %}
        <div class="flex_feature_item_teaser">
          <img src="{{ f.image_path | relative_url }}"
                alt="{% if f.alt %}{{ f.alt }}{% endif %}">
          {% if f.image_caption %}
            <span class="archive__item-caption">{{ f.image_caption | markdownify | remove: "<p>" | remove: "</p>" }}</span>
          {% endif %}
        </div>
      {% endif %}
      <div class="flex_feature_item_body">
        {% if f.title %}
          <h2 class="archive__item-title">{{ f.title }}</h2>
        {% endif %}
        {% if f.excerpt %}
          <div class="archive__item-excerpt">
            {{ f.excerpt | markdownify }}
          </div>
        {% endif %}
      </div>
      <div class="flex_feature_item_footer">
        {% if f.url %}
          <p><a href="{{ f.url | relative_url }}" class="btn {{ f.btn_class }}">{{ f.btn_label | default: site.data.ui-text[site.locale].more_label | default: "Learn More" }}</a></p>
        {% endif %}
      </div>
    </div>
  {% endfor %}
</div>
