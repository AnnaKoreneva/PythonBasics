# Naming convention:
# 1. Name of parameters is case-sensitive
# 2. Examples test , _test, first_test, TEST, Test - All of these are different parameters
# DATA TYPES:
# 1. Strings - enclosed in single or double quotes, immutable (operations cannot be performed)
# 2. Numbers: Integers - mutable, whole numbers
# 2. Numbers: Float - fractional numbers (decimals), mutable (2.14)
# 3. Boolean
# 4. Sequence:
#   - List
#   - Tuples
#   - Dictionaries
"""
Multiline comments
"""
# String formatting

first_mane = "Anna"
second_name = "Koreneva"
job_title = "Test Engineer"
print("{} {} works as a {}".format(first_mane, second_name, job_title))

my_int = 22
my_list = [1, "string_1", 1.1, 2.5, 6.8]
my_set = {1, "string_1", 1.1, 2.5, 6.8}  # CURLY BRACKETS!!! This is SET. Sets are unordered collections of unique
# elements. It needs to be converted to LIST

my_tuple = (9, 8, 7, 6)
my_dict = {"one": 1, "two": 2}

# print(my_list)
# print(my_tuple)
# print(my_dict)
# print(my_int)
# my_int = "www"  # re-declaring is available
# print(my_set)
# print(my_list[1])
# print(my_list[0:3])
# print(my_list[0:4:2])
# print(my_list[::-1])  # Inversion of the list [1, "string_1", 1.1, 2.5, 6.8]
# print("Please print " + str(123))  # Python is a typed language. Python need all items in the same format while

# concatenating values

my_str = "www"


# Global VS Local variables
def some_function():
    global my_str  # change the env value globally
    my_str = "test"
    print(my_str)


some_function()
print(my_str)

del my_str  # delete the parameter
print(my_str)
