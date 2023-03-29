from sys import stderr
from filecmp import cmp


def assert_file_equal(file1, file2, when_failure_print_message: str):
    if(cmp(file1, file2)) is False:
        print(when_failure_print_message, flush=True, file=stderr)
        raise AssertionError(locals())


def assert_file_not_equal(file1, file2, when_failure_print_message: str):
    if(cmp(file1, file2)) is True:
        print(when_failure_print_message, flush=True, file=stderr)
        raise AssertionError(locals())
