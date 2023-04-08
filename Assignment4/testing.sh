#!/bin/bash

# cppcheck-4
a=1
while [ "$a" -lt 93 ]
do
    ./cppcheck-test.sh cppcheck/cppcheck-4 $a
    a=$(( ${a}+1 ))
done


# cppcheck-8
a=1
while [ "$a" -lt 85 ]
do
    ./cppcheck-test.sh cppcheck/cppcheck-8 $a
    a=$(( ${a}+1 ))
done


# cppcheck-9
a=1
while [ "$a" -lt 86 ]
do
    ./cppcheck-test.sh cppcheck/cppcheck-9 $a
    a=$(( ${a}+1 ))
done


# cppcheck-10
a=1
while [ "$a" -lt 93 ]
do
    ./cppcheck-test.sh cppcheck/cppcheck-10 $a
    a=$(( ${a}+1 ))
done


# cppcheck-28
a=1
while [ "$a" -lt 85 ]
do
    ./cppcheck-test.sh cppcheck/cppcheck-28 $a
    a=$(( ${a}+1 ))
done
