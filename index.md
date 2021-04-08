---
title: "FLAMEGPU II is here..."
layout: splash
header:
  overlay_color: "#4d4d4d"
  overlay_particles: true
  actions:
    - label: "Download"
      url: "/download/"
excerpt: "The Flexible Large Scale Agent Modelling Environment for the Graphics Processing Unit (GPU)"
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

![FLAME GPU 2 logo]({{ "/assets/images/fgpu2_icon_256.png" | relative_url }}){: .align-right} FLAMEGPU is a GPU accelerated simulator for domain independent complex systems simulations. Version 2 brings a complete re-write of the existing library offering greater flexibility, an improved interface for agent scripting and better research software engineering. FLAMEGPU provides a mapping between a formal agent specifications with C based scripting and optimised CUDA code. This includes a number of key ABM building blocks such as multiple agent types, agent communication and birth and death allocation. The advantages of our contribution are three fold. Firstly Agent Based (AB) modellers are able to focus on specifying agent behaviour and run simulations without explicit understanding of CUDA programming or GPU optimisation strategies. Secondly simulation performance is significantly increased in comparison with desktop CPU alternatives. This allows simulation of far larger model sizes with high performance at a fraction of the cost of grid based alternatives. Finally massive agent populations can be visualised in real time as agent data is already located on the GPU hardware.

{% include feature_row %}

