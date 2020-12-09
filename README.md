[![Python Version](https://img.shields.io/pypi/pyversions/amap.svg)](https://pypi.org/project/amap)
[![PyPI](https://img.shields.io/pypi/v/amap.svg)](https://pypi.org/project/amap)
[![Wheel](https://img.shields.io/pypi/wheel/amap.svg)](https://pypi.org/project/amap)
[![Development Status](https://img.shields.io/pypi/status/amap.svg)](https://github.com/SainsburyWellcomeCentre/amap-python)
[![Travis](https://img.shields.io/travis/com/SainsburyWellcomeCentre/amap-python?label=Travis%20CI)](
    https://travis-ci.com/SainsburyWellcomeCentre/amap-python)
[![Coverage Status](https://coveralls.io/repos/github/SainsburyWellcomeCentre/amap-python/badge.svg?branch=master)](https://coveralls.io/github/SainsburyWellcomeCentre/amap-python?branch=master)
[![Dependabot Status](https://api.dependabot.com/badges/status?host=github&repo=SainsburyWellcomeCentre/amap-python)](https://dependabot.com)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/python/black)
[![Gitter](https://badges.gitter.im/cellfinder/amap.svg)](https://gitter.im/cellfinder/amap?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge)
[![DOI](https://zenodo.org/badge/225904061.svg)](https://zenodo.org/badge/latestdoi/225904061)


# amap-python
Automated mouse atlas propagation

**N.B. amap will not be developed further, in favour of 
[brainreg](https://github.com/brainglobe/brainreg), which is based on 
[bg-atlasapi](https://github.com/brainglobe/bg-atlasapi) to support multiple species,
atlases and resolutions.**


## About
amap is python software for registration of brain templates to sample whole-brain
microscopy datasets, and subsequent atlas-based segmentation by
[Adam Tyson](https://github.com/adamltyson), 
[Charly Rousseau](https://github.com/crousseau) & 
[Christian Niedworok](https://github.com/cniedwor) 
from the [Margrie Lab at the Sainsbury Wellcome Centre](https://www.sainsburywellcome.org/web/groups/margrie-lab).


This is a Python port of 
[aMAP](https://github.com/SainsburyWellcomeCentre/aMAP/wiki) (originally 
written in Java), which has been 
[validated against human segmentation](https://www.nature.com/articles/ncomms11879).

The actual registration is carried out by [NiftyReg](http://cmictig.cs.ucl.ac.uk/wiki/index.php/NiftyReg).

Documentation can be found [here](https://docs.cellfinder.info/amap/introduction).
## Details
The aim of amap is to register the template brain
 (e.g. from the [Allen Reference Atlas](https://mouse.brain-map.org/static/atlas))
  to the sample image. Once this is complete, any other image in the template
  space can be aligned with the sample (such as region annotations, for 
  segmentation of the sample image). The template to sample transformation
  can also be inverted, allowing sample images to be aligned in a common 
  coordinate space.
  
To do this, the template and sample images are filtered, and then registered in 
a three step process (reorientation, affine registration, and freeform 
registration.) The resulting transform from template to standard space is then
applied to the atlas. 
 
Full details of the process are in the 
[original paper](https://www.nature.com/articles/ncomms11879).
![process](https://raw.githubusercontent.com/SainsburyWellcomeCentre/amap-python/master/resources/reg_process.png)
**Overview of the registration process**

## Installation
```bash
pip install amap
```

## Usage
amap was designed with generality in mind, but is currently used for a single application. If anyone has different uses 
(e.g. requires a different atlas, or the data is in a different format), please get in touch 
by [email](mailto:adam.tyson@ucl.ac.uk?subject=amap) or by 
[raising an issue](https://github.com/SainsburyWellcomeCentre/amap-python/issues/new/choose).

### Basic usage
```bash
amap /path/to/raw/data /path/to/output/directory -x 2 -y 2 -z 5
```

### Arguments
#### Mandatory
* Path to the directory of the images. 
Can also be a text file pointing to the files.  
 * Output directory for all intermediate and final 
results

**Either**
* `-x` or `--x-pixel-um` Pixel spacing of the data in the first dimension, 
specified in um.
* `-y` or `--y-pixel-um` Pixel spacing of the data in the second dimension, 
specified in um.
* `-z` or `--z-pixel-um` Pixel spacing of the data in the third dimension, 
specified in um.

**Or**
* `--metadata` Metadata file containing pixel sizes (any format supported 
by [micrometa](https://github.com/adamltyson/micrometa) can be used).
  If both pixel sizes and metadata are provided, the command line arguments 
  will take priority.

#### Additional options
* `-d` or `--downsample` Paths to N additional channels to downsample to the 
same coordinate space.

Full command-line arguments are available with `amap -h`, but please 
[get in touch](mailto:adam.tyson@ucl.ac.uk?subject=amap) if you have any questions.


## Citing amap.

If you find amap useful, and use it in your research, please cite the [original Nature Communications paper](https://www.nature.com/articles/ncomms11879) along with this repository:

> Adam L. Tyson, Charly V. Rousseau, Christian J. Niedworok and Troy W. Margrie (2019). amap: automatic atlas propagation. [doi:10.5281/zenodo.3582162](https://zenodo.org/record/3582162)

**If you use this, or any other tools in the cellfinder suite, please
 [let us know](mailto:adam.tyson@ucl.ac.uk?subject=cellfinder-paper), and 
 we'd be happy to promote your paper/talk etc.**
 

## Visualisation
amap can use the 
[cellfinder visualisation function](https://docs.cellfinder.info/user-guide/visualisation) 
(built using [napari](https://github.com/napari/napari)).

#### Usage
```bash
cellfinder_view
```


![amap_viewer](https://raw.githubusercontent.com/SainsburyWellcomeCentre/amap-python/master/resources/amap_vis.gif)
