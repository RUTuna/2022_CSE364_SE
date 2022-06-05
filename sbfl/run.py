import utils
import os
from base import SBFL
import test_info

# Set variables
gcov_dir = test_info.CPPCHECK_28_TESTS
# test_info.CPPCHECK_4_TESTS
# test_info.EXAMPLE_TESTS
fail_tests = test_info.CPPCHECK_28_FAIL
# test_info.CPPCHECK_4_FAIL
# test_info.EXAMPLE_FAIL

# Read and parse gcov files
gcov_files = {test:[] for test in gcov_dir}
for test in gcov_dir:
    for path in os.listdir(gcov_dir[test]):
        if path.endswith('.gcov'):
            gcov_files[test].append(os.path.join(gcov_dir[test], path))
    print(f"{test}: {len(gcov_files[test])} gcov files are found.")

cov_df = utils.gcov_files_to_frame(gcov_files, only_covered=True)
print(cov_df)

# Run FL
result = utils.get_sbfl_scores_from_frame(cov_df, failing_tests=fail_tests,
                                          sbfl=SBFL('Ochiai'))

line_SBFL = result.line_SBFL
func_SBFL = result.func_SBFL
print('Ochiai\n', line_SBFL, '\n', func_SBFL)

start_index = 0
for i in range(4):
    start_index = gcov_dir['test1'].index('/', start_index)
    start_index = start_index + 1

end_index = gcov_dir['test1'].index('/gcov')
file_name = '/home/workspace/sbfl/csv/' + gcov_dir['test1'][start_index:end_index] + '_' + result.formula
line_SBFL.to_csv(file_name + '.csv', index=False)
func_SBFL.to_csv(file_name + '_function.csv')

# -----------------------------------------------------

result = utils.get_sbfl_scores_from_frame(cov_df, failing_tests=fail_tests,
                                          sbfl=SBFL('Tarantula'))

line_SBFL = result.line_SBFL
func_SBFL = result.func_SBFL
print('Tarantula\n', line_SBFL, '\n', func_SBFL)

start_index = 0
for i in range(4):
    start_index = gcov_dir['test1'].index('/', start_index)
    start_index = start_index + 1

end_index = gcov_dir['test1'].index('/gcov')
file_name = '/home/workspace/sbfl/csv/' + gcov_dir['test1'][start_index:end_index] + '_' + result.formula
line_SBFL.to_csv(file_name + '.csv', index=False)
func_SBFL.to_csv(file_name + '_function.csv')

# -----------------------------------------------------

result = utils.get_sbfl_scores_from_frame(cov_df, failing_tests=fail_tests,
                                          sbfl=SBFL('Jaccard'))

line_SBFL = result.line_SBFL
func_SBFL = result.func_SBFL
print('Tarantula\n', line_SBFL, '\n', func_SBFL)

start_index = 0
for i in range(4):
    start_index = gcov_dir['test1'].index('/', start_index)
    start_index = start_index + 1

end_index = gcov_dir['test1'].index('/gcov')
file_name = '/home/workspace/sbfl/csv/' + gcov_dir['test1'][start_index:end_index] + '_' + result.formula
line_SBFL.to_csv(file_name + '.csv', index=False)
func_SBFL.to_csv(file_name + '_function.csv')

# TODO: Save to csv file
