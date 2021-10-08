#!/bin/bash
#

set -e

SCRIPT_ROOT=$(cd -P -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd -P)
cd "${SCRIPT_ROOT}"

output="${SCRIPT_ROOT}"/archive.ics.uci.edu/ml/machine-learning-databases/poker

if [ ! -d "$output" ]; then
    mkdir -p "$output"
fi

dvc run -n poker-hand "${@}" \
    -d remote://uci/ml/machine-learning-databases/poker/poker-hand-testing.data \
    -d remote://uci/ml/machine-learning-databases/poker/poker-hand-training-true.data \
    -d remote://uci/ml/machine-learning-databases/poker/poker-hand.names \
    -o "${output}" \
    ./hack/download-external-dataset.sh
