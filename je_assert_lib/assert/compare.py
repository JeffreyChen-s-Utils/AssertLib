from sys import stderr


def assert_equal(assert_object1, assert_object2, when_failure_print_message: str):
    if assert_object1 != assert_object2:
        print(when_failure_print_message, flush=True, file=stderr)
        raise AssertionError(locals())


def assert_not_equal(assert_object1, assert_object2, when_failure_print_message: str):
    if assert_object1 == assert_object2:
        print(when_failure_print_message, flush=True, file=stderr)
        raise AssertionError(locals())
