#!/usr/bin/env bash

set -ex

JOB_PATH=$(r3 commit $1)
JOB_ID=$(basename $JOB_PATH)

if [ -z "$SCRATCH" ]; then
    SCRATCH=${HOME/home/scratch_local}
fi
echo "SCRATCH=$SCRATCH"

WORK_DIR="$SCRATCH/jobs"
mkdir -p $WORK_DIR
r3 checkout $JOB_PATH "$WORK_DIR/$JOB_ID"
cd "$WORK_DIR/$JOB_ID"
./run.sh
