#!/bin/bash
#
#   Download poker hands from uci
#
#   dvc run -n download_file \
#       -d archive.ics.uci.edu/ml/machine-learning-databases/poker/poker-hand-testing.data \
#       -d archive.ics.uci.edu/ml/machine-learning-databases/poker/poker-hand-training-true.data \
#       -d archive.ics.uci.edu/ml/machine-learning-databases/poker/poker-hand.names \
#       -o archive.ics.uci.edu/ml/machine-learning-databases/poker \
#       ./hack/download-external-dataset.sh

set -e

wget -r -np -R "index.html*" https://archive.ics.uci.edu/ml/machine-learning-databases/poker/
