#!/usr/bin/env bash

set -e

singularity exec --bind /mnt/qb --bind $PWD --pwd $PWD container.sif python3 run.py
