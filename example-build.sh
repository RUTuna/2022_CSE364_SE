#!/bin/bash

if [ "$#" -ne 1 ]; then
    echo "Usage: ./example-build.sh <project path>"
    exit 1
fi

cur_dir=`pwd`
cd $1
make clean
make CFLAGS="-fprofile-arcs -ftest-coverage -g -O0"
