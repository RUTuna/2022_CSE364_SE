#!/bin/bash

if [ "$#" -ne 1 ]; then
    echo "Usage: ./cppcheck-build.sh <project path>"
    exit 1
fi

cd $1
rm -rf build
cmake -Wno-dev -DCMAKE_C_FLAGS="--coverage -g -O0" -DCMAKE_CXX_FLAGS="--coverage -g -O0" -DCMAKE_CXX_OUTPUT_EXTENSION_REPLACE=ON -DCMAKE_C_OUTPUT_EXTENSION_REPLACE=ON -DBUILD_TESTS=ON -S . -B build
cmake --build build --target clean
bear cmake --build build --target all
