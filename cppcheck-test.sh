#!/bin/bash

if [ "$#" -lt 2 ]; then
    echo "Usage: ./cppcheck-test.sh <project path> <test number>"
    exit 1
fi

cd $1
# Run test
echo $2 > DPP_TEST_INDEX
bash -c "[ -f CTEST_TEST_CASE.output ] || ctest --show-only --test-dir build | sed -rn 's/[[:blank:]]*Test[[:blank:]]*#[[:digit:]]*:[[:blank:]]*(.*)/\\1/p' > CTEST_TEST_CASE.output"
bash -c 'index=$(cat DPP_TEST_INDEX); ctest --output-on-failure --tests-regex $(sed -n "${index}p" < CTEST_TEST_CASE.output)$ --test-dir build'

# Generate gcov files
file=gcov/test$2
if [ -d "$file" ]
then
    rm -rf $file
fi
mkdir $file
find build/cli/CMakeFiles/cppcheck.dir -type f -name "*.o" -exec gcov -b --preserve-paths  {} \;
find build/cli/CMakeFiles/cli_objs.dir -type f -name "*.o" -exec gcov -b --preserve-paths  {} \;
find build/lib/CMakeFiles/lib_objs.dir -type f -name "*.o" -exec gcov -b --preserve-paths  {} \;
rm -rf *.gcda
mv *.gcov $file

