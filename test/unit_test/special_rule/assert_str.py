from je_assert_lib import assert_str_is_alnum, assert_str_is_not_alnuma

try:
    assert_str_is_alnum("I'm not empty")
except AssertionError:
    print("That's right")

try:
    assert_str_is_not_alnuma("12345")
except AssertionError:
    print("That's right")
