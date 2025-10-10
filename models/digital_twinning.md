---
title: "Digital Twinning of Urban Transportation Systems with Fujitsu Research Europe "
permalink: "models/digital-twinning"
---

![Digital Twinning of Urban Transportation Systems Road Network Model Close-up]({{ "/assets/images/models/digital-twinning.png" | relative_url }}){: .align-right .no-shadow} 

In collaboration with Fujitsu Research of Europe, the FLAME GPU team undertook a collaborative development project to assist in applying FLAME GPU to the simulation of urban transportation systems in order to create a digital twin of the Isle of Wight. The focus of model development was on transportation micros simulation and road networks (junctions). The developed model aims to replicate a subset of the individual and junction models from the open source Simulation of Urban MObility (SUMO) within FLAME GPU. Computational experiments have indicated that speedups over SUMO of ~68x are achievable on desktop GPUs (Intel Core i7-5930K CPU, an NVIDIA GeForce RTX 3090 (24 GiB) GPU). This is equivalent to simulating ~100x faster than real time with a maximum load of 95k vehicles.


## More Information

 - Smilovitskiy et al. "FLAME-GPU for Traffic Systems: A Scalable Agent-Based Simulation Framework." *Systems 2025, 13, 376. https://doi.org/10.3390/systems13050376* [Research Paper](https://www.mdpi.com/2079-8954/13/5/376) 

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/hZPDgZZP5TM?si=MVQ6LhFkrcweuYay" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>