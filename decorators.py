# A decorator is a function that takes another function and extends the behavior of the latter function without
# explicitly modifying it.
# In Python, functions are first-class objects. This means that functions can be passed around and used as arguments,
# just like any other object (string, int, float, list, and so on).

def say_hello(name):
    return f"Hello {name}"


def be_awesome(name):
    return f"Yo {name}, together we are the awesome!"


def greet_bob(greeter_func):
    return greeter_func("Bob")


print(greet_bob(be_awesome))
print(greet_bob(say_hello))
