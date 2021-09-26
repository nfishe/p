#!/bin/bash
#

set -e

SCRIPT_ROOT=$(cd -P -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd -P)
cd "${SCRIPT_ROOT}"

output="${SCRIPT_ROOT}"/archive.ics.uci.edu/ml/machine-learning-databases/poker

if [ ! -d "$output" ]; then
    mkdir -p "$output"
fi

dvc run -n poker-hand \
    -d https://archive.ics.uci.edu/ml/machine-learning-databases/poker/poker-hand-testing.data \
    -d https://archive.ics.uci.edu/ml/machine-learning-databases/poker/poker-hand-training-true.data \
    -d https://archive.ics.uci.edu/ml/machine-learning-databases/poker/poker-hand.names \
    -o "${output}" \
    wget -r -np -R "index.html*" https://archive.ics.uci.edu/ml/machine-learning-databases/poker/
