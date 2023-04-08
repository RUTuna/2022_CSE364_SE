#!/bin/bash

if [ "$#" -lt 2 ]; then
    echo "Usage: ./example-test.sh <project path> <test number>"
    exit 1
fi

cd $1
# Run test
./test $(expr $2 - 1)

# Generate gcov files
file=gcov/test$2
if [ -d "$file" ]
then
    rm -rf $file
fi
mkdir $file
find . -type f -name "*.gcno" -execdir gcov -b --preserve-paths  {} \;
rm -rf *.gcda
mv *.gcov $file

