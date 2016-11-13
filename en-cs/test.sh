#!/bin/bash
set -o nounset
set -o errexit

cd `dirname $0`
./sort.sh check

# TODO: doplnit kontrolu formatu
