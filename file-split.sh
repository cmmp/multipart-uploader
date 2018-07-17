#!/bin/bash
FILE=$1
mkdir -p parts/
rm -f parts/part*

split -a 2 --numeric-suffixes=1 -n 20 --verbose ${FILE} parts/part-
