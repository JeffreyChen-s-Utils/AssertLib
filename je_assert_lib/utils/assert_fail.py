from sys import stderr


def assert_fail_message(when_failure_print_message: str):
    print(when_failure_print_message, flush=True, file=stderr)
    raise AssertionError
