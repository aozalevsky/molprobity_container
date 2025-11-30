# Apptainer container for MolProbity

[![License:
MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This repository contains build recipes for an
[Apptainer](https://apptainer.org/) (formerly Singularity) container
image of the [MolProbity](https://github.com/rlabduke/MolProbity)
software suite, used for assessment of macromolecular
structure models.

## Contents

The container provides:

-   MolProbity and its standard tools
-   All required dependencies pre-installed
-   A command-line entry point for running MolProbity on your structure
    files

> **Note:** This repository only contains the container build recipe.
> You build the image locally using Apptainer/Singularity.

------------------------------------------------------------------------

## Requirements

-   Apptainer **or** SingularityCE installed on your system
-   `git` for cloning this repository
-   Sufficient disk space to build and store the image

------------------------------------------------------------------------

## Installation

Clone this repository and build the container image:

``` bash
git clone https://github.com/aozalevsky/molprobity_container
cd molprobity_container

# Using Apptainer
apptainer build molprobity.sif Singularity.def

# Or, with older Singularity
singularity build molprobity.sif Singularity.def
```

This will create a `molprobity.sif` image in the current directory.

------------------------------------------------------------------------

## Usage

### Basic example

To run MolProbity on the example structure file:

``` bash
./molprobity.sif molprobity.molprobity example/1MBN.cif
```

Or, explicitly via Apptainer:

``` bash
apptainer exec molprobity.sif molprobity.molprobity example/1MBN.cif
```

### Using your own data

If your input files live elsewhere on your filesystem, you may want to
bind-mount that directory into the container:

``` bash
apptainer exec   --bind /path/to/data:/data   molprobity.sif   molprobity.molprobity /data/your_model.cif
```

Replace `/path/to/data` and `your_model.cif` with your actual paths and
filenames.

### Interactive shell (optional)

To explore the container interactively:

``` bash
apptainer shell molprobity.sif
```

From inside the container, you can run MolProbity commands directly.

------------------------------------------------------------------------

## Citation

If you use MolProbity in published work, please cite the MolProbity
papers as described in the official MolProbity documentation and
[repository](https://github.com/rlabduke/MolProbity).

------------------------------------------------------------------------

## License

This project is licensed under the MIT License.\
See the `LICENSE` file for details.

------------------------------------------------------------------------

## Maintainer

Maintained by **Arthur Zalevsky** <<aozalevsky@gmail.com>>

Bug reports and feature requests are welcome via GitHub Issues.
