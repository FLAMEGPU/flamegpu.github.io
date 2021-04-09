---
title: "Download FLAME GPU"
---

## FLAME GPU 2.x

[![FLAME GPU 2 logo]({{ "/assets/images/fgpu2_icon_256.png" | relative_url }})](https://github.com/FLAMEGPU/FLAMEGPU2){: .align-right .no-shadow} 
FLAME GPU 2 is currently in an alpha release phase as new features are integrated to support ongoing projects.
As the API is not yet finalised there may be be breaking changes as development continues.

It is mostly feature complete with FLAME GPU 1 but may not meet the same levels of performance for all use cases.
This is a result of the vastly more flexible interface used to template generated code.
Performance is generally still very close to or better than FLAME GPU 1 and optimisations are always being added.

FLAME GPU 2 uses [CMake](https://cmake.org) as a cross-platform build system, with support for Windows via Visual Studio and for linux systems via make, with support for CUDA 10.0+.
Please see the [readme](https://github.com/FLAMEGPU/FLAMEGPU2) for further information on the dependencies of FLAME GPU 2 and the model development process.

To use FLAME GPU 2, you can either start by consider starting with one of the standalone [models](../models), or create a new standalone model based on the [template repository](https://github.com/FLAMEGPU/FLAMEGPU2-example-template) or by downloading and building the main [FLAME GPU 2](https://github.com/FLAMEGPU/FLAMEGPU2) project and follow the instructions in the readme.

## FLAME GPU 1.x

[![FLAME GPU 1 logo]({{ "/assets/images/flame_gpu_v1.jpg" | relative_url }})](https://github.com/FLAMEGPU/FLAMEGPU){: .align-right .no-shadow} 
FLAME GPU 1.x releases are still available to download and use, although there are no plans for further development of FLAME GPU 1.
The latest release, FLAME GPU 1.5 supports CUDA 10.2 with Visual Studio 2015/2019 on windows and Make on Linux). 
CUDA 11.0+ is unsupported.

 * [Download FLAME GPU 1.5 SDK release for CUDA 10.2](https://github.com/FLAMEGPU/FLAMEGPU/releases/download/v1.5.0/FLAME-GPU-SDK.zip)
 * [FLAME GPU 1.5.x on GitHub](https://github.com/FLAMEGPU/FLAMEGPU)

The FLAME GPU 1 SDK requires an installation of a CUDA toolkit and compatible driver. 
The .zip download includes windows executables for each example model in the 'bin' folder for a x64 architecture.
Visual studio 2015 project files are included for each of the SDK examples. 
These include custom build rules for FLAME GPU template processing and the CUDA build step (further details are provided in the documentation section of this site).