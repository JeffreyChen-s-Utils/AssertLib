from je_assert_lib import assert_is_not_dir, assert_is_dir

try:
    assert_is_not_dir("test2")
except AssertionError:
    print("That's right")

try:
    assert_is_dir("test")
except AssertionError:
    print("That's right")
