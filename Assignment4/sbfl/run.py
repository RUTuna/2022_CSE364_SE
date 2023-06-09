import utils
import os
from base import SBFL
import test_info

# Set variables
gcov_dir = test_info.EXAMPLE_TESTS
# test_info.CPPCHECK_4_TESTS
# test_info.EXAMPLE_TESTS
fail_tests = test_info.EXAMPLE_FAIL
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
for method in ['Ochiai', 'Tarantula', 'Jaccard']:
    result = utils.get_sbfl_scores_from_frame(cov_df, failing_tests=fail_tests,
                                          sbfl=SBFL(method))

    line_SBFL = result.line_SBFL
    func_SBFL = result.func_SBFL
    print(method, '\n', line_SBFL, '\n', func_SBFL)

    start_index = 0
    for i in range(4):
        start_index = gcov_dir['test1'].index('/', start_index)
        start_index = start_index + 1

    end_index = gcov_dir['test1'].index('/gcov')
    file_name = '/home/workspace/sbfl/csv/' + gcov_dir['test1'][start_index:end_index] + '_' + result.formula.lower()
    line_SBFL.to_csv(file_name + '.csv', index=False, quotechar='!')
    func_SBFL.to_csv(file_name + '_function.csv', quotechar='!')

# TODO: Save to csv file
