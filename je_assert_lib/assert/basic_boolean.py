from sys import stderr


def assert_true(assert_object1, when_failure_print_message: str):
    if (bool(assert_object1)) is False:
        print(when_failure_print_message, flush=True, file=stderr)
        raise AssertionError(locals())


def assert_false(assert_object1, assert_object2, when_failure_print_message: str):
    if (bool(assert_object1)) is True:
        print(when_failure_print_message, flush=True, file=stderr)
        raise AssertionError(locals())


def assert_is(assert_object1, assert_object2, when_failure_print_message: str):
    if assert_object1 is not assert_object2:
        print(when_failure_print_message, flush=True, file=stderr)
        raise AssertionError(locals())


def assert_is_not(assert_object1, assert_object2, when_failure_print_message: str):
    if assert_object1 is assert_object2:
        print(when_failure_print_message, flush=True, file=stderr)
        raise AssertionError(locals())


def assert_is_none(assert_object1, when_failure_print_message: str):
    if assert_object1 is not None:
        print(when_failure_print_message, flush=True, file=stderr)
        raise AssertionError(locals())


def assert_is_not_none(assert_object1, when_failure_print_message: str):
    if assert_object1 is None:
        print(when_failure_print_message, flush=True, file=stderr)
        raise AssertionError(locals())
