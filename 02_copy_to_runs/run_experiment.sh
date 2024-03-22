#!/usr/bin/env bash

set -ex

mkdir -p runs
run_id=$(uuidgen -r)
cp -r $1 runs/$run_id
cd runs/$run_id
./run.sh
