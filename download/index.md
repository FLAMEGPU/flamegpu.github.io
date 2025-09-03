---
title: "Download FLAME GPU"
---

## FLAME GPU 2+

The simplest and recommend way to install FLAME GPU 2+ is to install our pre-built python binary wheels using our [wheelhouse](https://whl.flamegpu.com/). E.g. to install the latest pyflamegpu build for CUDA 12.0+ with visualiastion:

```
python3 -m pip install --extra-index-url https://whl.flamegpu.com/whl/cuda120-vis/ pyflamegpu
```

Please see the [Release Notes](https://github.com/FLAMEGPU/FLAMEGPU2/releases/latest) for more information.

To build FLAME GPU 2+ or develop using C++, you can either start by consider starting with one of the standalone [models](../models), or create a new standalone model based on the [template repository](https://github.com/FLAMEGPU/FLAMEGPU2-example-template) or by downloading and building the main [FLAME GPU 2](https://github.com/FLAMEGPU/FLAMEGPU2) project and follow the instructions in the readme. FLAME GPU 2 uses [CMake](https://cmake.org) as a cross-platform build system, with support for Windows via Visual Studio and for Linux systems via make, with support for CUDA 12.0+. Please see the [readme](https://github.com/FLAMEGPU/FLAMEGPU2) for further information on the dependencies of FLAME GPU 2 and the model development process.

FLAME GPU 2 is released under a [dual licence of AGPL v3.0 and a commercial licence](./licence). Pre-release versions were previously distributed under MIT.

*Note: FLAME GPU 2 refers to Versions 2+ as opposed to the legacy 1.x version of FLAME GPU*



## FLAME GPU 1.x (Legacy Versions)

[![FLAME GPU 1 logo]({{ "/assets/images/flame_gpu_v1.jpg" | relative_url }})](https://github.com/FLAMEGPU/FLAMEGPU){: .align-right .no-shadow} 
FLAME GPU 2 is designed on the same concepts and ideas of FLAME GPU 1 with a similar but vastly improved interface and wider variety of features. FLAME GPU 1.x releases are still available to download and use, although it should be considered legacy software and there are no plans for further development or maintenance of FLAME GPU 1.

The latest release, FLAME GPU 1.5 supports CUDA 10.2 with Visual Studio 2015/2019 on windows and Make on Linux). 
CUDA 11.0+ is unsupported.

* [Download FLAME GPU 1.5 SDK release for CUDA 10.2](https://github.com/FLAMEGPU/FLAMEGPU/releases/download/v1.5.0/FLAME-GPU-SDK.zip)
* [FLAME GPU 1.5.x on GitHub](https://github.com/FLAMEGPU/FLAMEGPU)

The FLAME GPU 1 SDK requires an installation of a CUDA toolkit and compatible driver. 
The .zip download includes windows executables for each example model in the 'bin' folder for a x64 architecture.
Visual studio 2015 project files are included for each of the SDK examples. 
These include custom build rules for FLAME GPU template processing and the CUDA build step (further details are provided in the documentation section of this site).