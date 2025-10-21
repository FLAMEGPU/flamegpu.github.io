---
title: "Simulating Plastic Strain Accumulation in Rail Steel"
permalink: "models/rail-steel"
---

![Plastic Strain Accumulation in Rail Steel 3D Render]({{ "/assets/images/models/rail-steel.png" | relative_url }}){: .align-right .no-shadow} 

The modelling of plastic strain accumulation in rail steels, a process that is the root cause of a number of rail failure mechanisms, is generally a complex and computationally expensive task. Finite element techniques are usually limited to simulating only a few hundred wheel passes, which is representative of only a few hours of the in-service life of a rail. Thus, there exists a demand for methods that reduce the computation time required in order to better understand the long-term behaviour of rail materials. 

The Dynarat technique, an established method of simulation which represents rail response by discretising a section of rail material into bricks which accumulate strain in response to the maximum orthogonal shear stress experienced each cycle, was translated into an agent-based materials model using FLAMEGPU. 

Each material agent accumulates strain, in response to each wheel pass, in parallel. This allows for faster simulations of tens of thousands of cycles. With the reduction in computational expense, larger scale, 3d simulations with microstructurally distributed properties, can be introduced. Moreover, agent-based modelling facilitates communication between material agents, such that they can exchange information about their respective strain states and any discontinuities between them. 

This has facilitated the introduction of a novel failure mechanism which represents the effect of strain partitioning between microstructural constituents which could not have been represented before.


## More Information

 - [Featured on Page67 of “Rail Engineer magazine](https://www.railengineer.co.uk/rail-engineer-march-april-2025-rules-do-they-keep-track-workers-safe-better-possession-protection-hs2s-delta-junction/)

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/_jRZMfsbwsw?si=wS36YXPbkb9YIkxW" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>