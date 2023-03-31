from je_assert_lib import assert_file_equal, assert_file_not_equal

with open("test1.txt", "w+") as file:
    file.write("test")

with open("test2.txt", "w+") as file:
    file.write("test")

with open("test3.txt", "w+") as file:
    file.write("test ooo")

try:
    assert_file_equal("test1.txt", "test3.txt")
except AssertionError:
    print("That's right")


try:
    assert_file_not_equal("test1.txt", "test2.txt")
except AssertionError:
    print("That's right")


