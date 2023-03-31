from je_assert_lib import assert_file_exists, assert_file_not_exists

with open("test1.txt", "w+") as file:
    file.write("test")

try:
    assert_file_exists("test2.txt")
except AssertionError:
    print("That's right")

try:
    assert_file_not_exists("test1.txt")
except AssertionError:
    print("That's right")
