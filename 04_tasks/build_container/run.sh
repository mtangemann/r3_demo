#!/usr/bin/env bash

set -e

mkdir -p output
singularity build --fakeroot output/container.sif container.def
