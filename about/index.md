---
title: "About FLAME GPU"
---

![GPU melting into a flock of birds]({{ "/assets/images/gpu_birds.png" | relative_url }}){: .align-center}

FLAME GPU has the aim of accelerating the performance and scale of agent based simulation by targeting readily available parallelism in the form of Graphics Processing Units (GPUs). A central idea behind FLAME GPU is to abstract the GPU away from modellers so that modellers can build models without having to worry about writing parallel code. FLAME GPU also separates a model description from the model implementation. This simplifies the processes of validating and verifying models as the simulator code is tested in isolation from the model itself.

FLAME GPU started in the early days of general purpose computing on GPUs. GPU hardware and software development approaches have changed significantly since the inception of FLAME GPU, as such version 2.0 is a complete re-write of the library. It shifts from the FLAME GPU 1 architecture of template driven agent based modelling towards a modern C++ API with a cleaner interface for the specification of agent behaviour. It also adds a range of new features which ensure performant model simulation. E.g.

* **Support for Big GPUs** - Support for concurrent execution of agents functions which ensures that heterogenous models do not necessarily result in poor device utilisation.
* **Model Ensembles** - The ability to run ensembles of models. I.e. the same model with different parameters or random seeds. This is necessary within stochastic simulation and FLAME GPU allows the specification of ensembles to occupy multiple devices on a single computing node.
* **Sub models** - Certain behaviours in FLAME GPU require iterative processes to ensure reproducibility with serial counterparts (e.g. conflict resolution for resources). FLAME GPU 2 allows re-usable sub models to be described for such behaviours so that it can be abstracted from the rest of the model function.

FLAME GPU 2 is available under a dual [Open Source and commercial license](http://127.0.0.1:4000/download/license/). For commercial consultancy using the software please [contact us](/contact/).

For an introduction to FLAME GPU 2 and its features (in Apr 2021) please view the [GTC 2021 recorded talk](https://gtc21.event.nvidia.com/media/Simulate%20the%20World%20and%20Everything%20in%20it%3A%20Complex%20Systems%20Simulations%20with%20FGPU2%20%5BE31281%5D/1_jq4vdfcg) (requires free registration) by Paul Richmond (youtube copy embedded below).

<iframe width="560" height="315" src="https://www.youtube.com/embed/NRRW6EDClYM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>




## Publications

There are [a number of papers](/publications/) which describe novel aspects of the way FLAME GPU has been designed and implemented. These do not include papers of specific model implementations which can generally be found in the citations section.

To cite FLAME GPU 2.x please cite the FLAME GPU 2 software as:

> *P. Richmond, R. Chisholm, P. Heywood, M. Leach, and M. Kabiri Chimeh*, FLAME GPU. Zenodo, 2021. doi: [10.5281/ZENODO.5428984](https://doi.org/10.5281/zenodo.5428984).

<!-- @todo - add paper citation. -->

To cite FLAME GPU 1.x please cite;

> *P. Richmond, D. Walker, S. Coakley, and D. Romano*, ‘High performance cellular level agent-based simulation with FLAME for the GPU’, Briefings in Bioinformatics, vol. 11, no. 3, pp. 334–347, Feb. 2010, doi: [10.1093/bib/bbp073](https://doi.org/10.1093/bib/bbp073).

<!-- ```
@article{richmond2010high,
  title={High performance cellular level agent-based simulation with FLAME for the GPU},
  author={Richmond, Paul and Walker, Dawn and Coakley, Simon and Romano, Daniela},
  journal={Briefings in bioinformatics},
  volume={11},
  number={3},
  pages={334--347},
  year={2010},
  publisher={Oxford University Press}
}
``` -->

## Citations

There are {{ site.data.citations.size }} citations of the publications which describe FLAME GPU. You can view a [list of these in order of the number of citations that they have received](/citations/).
