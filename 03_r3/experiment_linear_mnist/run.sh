#!/usr/bin/env bash

set -e

mkdir -p output/data
singularity build --fakeroot output/container.sif container.def

PWD=$(realpath $(dirname $0))
singularity exec --bind /mnt/qb --bind $PWD --pwd $PWD output/container.sif python3 prepare_mnist.py
singularity exec --bind /mnt/qb --bind $PWD --pwd $PWD output/container.sif python3 train.py
