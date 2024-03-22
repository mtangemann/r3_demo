#!/usr/bin/env bash

set -e

mkdir -p data
singularity build --fakeroot data/container.sif container.def

PWD=$(realpath $(dirname $0))
singularity exec --bind $PWD --pwd $PWD data/container.sif python3 prepare_mnist.py
singularity exec --bind $PWD --pwd $PWD data/container.sif python3 train.py
