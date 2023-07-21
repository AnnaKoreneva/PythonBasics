# Conditions is about making decisions
# Comparison operators: >, <, >=, <=, ==, !=
# Once the condition is met, none of the other conditions matter

# print(1 > 1)
# print(1 != 1)
# print(1 == 1)

# name = input("What is your name? ")
# if name == "Anna":
#     print("Hello. Nice to see you {}".format(name))
# elif name == "Anton":
#     print("Oh! {}, you are my husband, let's have dinner".format(name))
# else:
#     print("Hello, {}! The access is denied".format(name))
# print("Have a nice day!")

def add():
    a = float(input("Please add the first number "))
    b = float(input("Please add the second number "))
    print(a + b)


def subtraction():
    a = float(input("Please add the first number "))
    b = float(input("Please add the second number "))
    print(a - b)


def multiply():
    a = float(input("Please add the first number "))
    b = float(input("Please add the second number "))
    print(a * b)


def divide():
    a = float(input("Please add the first number "))
    b = float(input("Please add the second number "))
    if b != 0:
        print(a / b)
    else:
        print("Sorry division to 0 is prohibit")


# if operation == "+":
#     add()
# elif operation == "-":
#     subtraction()
# elif operation == "*":
#     multiply()
# elif operation == "/":
#     divide()
# else:
#     print("That operation is not available")

# from python 3.10 ; | - OR ; || - AND
on = True

while on:
    operation = input("Please choose +, -, *, / or type q for quit")
    match operation:
        case "+":
            add()
        case "-":
            subtraction()
        case "*":
            multiply()
        case "/":
            divide()
        case "q":
            print("Sad to see that you finished the program")
            on = False  # OR break could be used as well
        case _:
            print("That operation is not available")
