import sys


def assert_true(assert_object1, when_failure_print_message):
    if (bool(assert_object1)) is not True:
        print(when_failure_print_message, flush=True, file=sys.stderr)
        raise AssertionError(locals())


def assert_false(assert_object1, assert_object2, when_failure_print_message):
    if (bool(assert_object1)) is True:
        print(when_failure_print_message, flush=True, file=sys.stderr)
        raise AssertionError(locals())
