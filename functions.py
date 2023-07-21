# Unit of code that will be reused through the code
# Function is an object which could be passed around in the code and should be defined
"""
POSITIONAL ARGUMENTS:
def func (f_name, l_name, age) / f_name, l_name, age are positional arguments because Python is reading
these arguments_ in order_, in the position that they are given in the function definition

KEYWORD ARGUMENTS
We can set some default values. F.e def func (f_name, l_name, age = 0) / Age is keyword arg because it has the default
With keyword arguments, you don't need to follow the positional order of the argument.

All three types of arguments might be used in a single function. They MUST BE used in an order:
 positional args -> *args -> **kwargs
"""

# function without arg
def function1():
    print("I am a function")


# func with an arguments
def function2(num1, num2):
    print(num1 + num2)


# function which returns argument
def function3(x):
    return x * x * x


# The function with default value of arguments
def function4(num, x=1):
    result = 1
    for i in range(x):
        result = result * num
    return result


# Function with the verity number of arguments
def function5(*args):
    result = 0
    for i in args:
        result = result + i
    return result


def func6(f_name, l_name, *args, age=0, position=" "):
    print("{} {} works at {} and has salary {}. Employee age is {} and position is {}".format(f_name, l_name, *args, age, position))


# function2(20, 30)
# print(function2(2, 3))  # Two rows are returned: first is the value and second is None because function has nothing
# # to return
# print(function3(3))

# print(function4(2))
# print(function4(2, 3))
# print(function4(x=4, num=5))  # we can change parameters place, but we need to mention parameter name.
# # We may include name parameters but all of them should go BEFORE the *args / def func5(arg1, *args):...
# print(function5(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
# print(function5(10, 80))

func6("Anna", "Koreneva", "Sigma Software", 6000, age=31, position="Test Eng")



