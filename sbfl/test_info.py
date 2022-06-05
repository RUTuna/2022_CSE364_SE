CPPCHECK_4_SIZE=92
CPPCHECK_8_SIZE=84
CPPCHECK_9_SIZE=85
CPPCHECK_10_SIZE=92
CPPCHECK_28_SIZE=84
EXAMPLE_SIZE=5

CPPCHECK_4_TESTS = {}
for i in range(1, CPPCHECK_4_SIZE+1):
    CPPCHECK_4_TESTS[f'test{i}'] = f'/home/workspace/cppcheck/cppcheck-4/gcov/test{i}'
CPPCHECK_4_FAIL = ['test21']

CPPCHECK_8_TESTS = {}
for i in range(1, CPPCHECK_8_SIZE+1):
    CPPCHECK_8_TESTS[f'test{i}'] = f'/home/workspace/cppcheck/cppcheck-8/gcov/test{i}'
CPPCHECK_8_FAIL = ['test32']

CPPCHECK_9_TESTS = {}
for i in range(1, CPPCHECK_9_SIZE+1):
    CPPCHECK_9_TESTS[f'test{i}'] = f'/home/workspace/cppcheck/cppcheck-9/gcov/test{i}'
CPPCHECK_9_FAIL = ['test5']

CPPCHECK_10_TESTS = {}
for i in range(1, CPPCHECK_10_SIZE+1):
    CPPCHECK_10_TESTS[f'test{i}'] = f'/home/workspace/cppcheck/cppcheck-10/gcov/test{i}'
CPPCHECK_10_FAIL = ['test15']

CPPCHECK_28_TESTS = {}
for i in range(1, CPPCHECK_28_SIZE+1):
    CPPCHECK_28_TESTS[f'test{i}'] = f'/home/workspace/cppcheck/cppcheck-28/gcov/test{i}'
CPPCHECK_28_FAIL = ['test5']

EXAMPLE_TESTS = {}
for i in range(1, EXAMPLE_SIZE+1):
    EXAMPLE_TESTS[f'test{i}'] = f'/home/workspace/example/example-1/gcov/test{i}'
EXAMPLE_FAIL = ['test3']
