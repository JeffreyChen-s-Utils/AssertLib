import sys


def assert_equal(assert_object1, assert_object2, when_failure_print_message):
    if not (assert_object1 == assert_object2):
        print(when_failure_print_message, flush=True, file=sys.stderr)
        raise AssertionError(locals())


def assert_not_equal(assert_object1, assert_object2, when_failure_print_message):
    if assert_object1 == assert_object2:
        print(when_failure_print_message, flush=True, file=sys.stderr)
        raise AssertionError(locals())
