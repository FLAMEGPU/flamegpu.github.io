---
title: "Download FLAME GPU"
---

![FLAME GPU 2 logo]({{ "/assets/images/fgpu2_icon_256.png" | relative_url }}){: .align-left} FLAME GPU 2 is currently in a Beta release phase as new features are integrated to support ongoing projects. It is feature complete with FLAME GPU 1 but may not meet the same levels of performance for all use cases. This is a result of the vastly more flexible interface used to template generated code. Performance is generally still very close to or better than FLAME GPU 1 and optimisations are always being added.

FLAME GPU 2 uses CMake, as a cross-platform process, for configuring and generating build directives, e.g. Makefile or .vcxproj. This is used to build the FLAMEGPU2 library, examples, tests and documentation. To download FLAME GPU 2 you should ideally start with an [example model](/models/). Each example model will clone the main FLAME GPU 2 library as part of the cmake build process. Alternatively you can download and build the main FLAME GPU 2 repository by first installing cmake and then following the instructions in the [main repository readme.md](https://github.com/FLAMEGPU/FLAMEGPU2)

## Older Versions of FLAME GPU (<2.0)

![FLAME GPU 1 logo]({{ "/assets/images/flame_gpu_v1.jpg" | relative_url }}){: .align-right} If you are looking for older version of FLAME GPU then you can still download these. The latest version 1 release is FLAME GPU 1.5 SDK which supports CUDA 10.2 with Visual Studio 2015/2019 (and Linux).

 * [Download FLAME GPU 1.5 release for CUDA 10.2](https://github.com/FLAMEGPU/FLAMEGPU/releases/download/v1.5.0/FLAME-GPU-SDK.zip)
 * [FLAME GPU 1.5.X master branch on GitHub](https://github.com/FLAMEGPU/FLAMEGPU)

The FLAME GPU 1 SDK requires an installation of a CUDA toolkit and compatible driver. Binary windows executables are provided for each of the SDK in the 'bin' folder for a x64 architecture. Visual studio 2015/2019 project files are included for each of the SDK examples. These include custom build rules for FLAME GPU template processing and the CUDA build step (further details are provided in the documentation section of this site).