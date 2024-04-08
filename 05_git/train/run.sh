#!/usr/bin/env bash

set -e

singularity exec --bind /mnt/qb --bind $PWD --pwd $PWD --env PYTHONPATH=image_grid container.sif python3 run.py
