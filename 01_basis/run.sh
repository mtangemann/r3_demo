#!/usr/bin/env bash

set -e

mkdir -p data
singularity build --fakeroot data/container.sif container.def

singularity exec data/container.sif python3 prepare_mnist.py
singularity exec data/container.sif python3 train.py
