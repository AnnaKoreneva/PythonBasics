"""
There are two types of loops in python:
- while - A while loop will run any time a condition remains true.
- for - is useful to iterate over each item in a list

LOOP controls
Continue - Skips current part of the loop, moves to the next part
Break - end the loop. Go to the next statement of the program
Pass - skips any part of the loop where pass appears

"""
# days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
# for day in days:
#     if day == "Sun":
#         print("This is a weekend!")
#         break  # Break the loop and quit
#     print(day)
#
# for number in range(10, 20, 2):
#     print("This number is {}".format(number))

temp = 30
while temp > 20:
    print("The tem is {}. It is pretty hot outside".format(temp))
    temp -= 1
    if temp == 25:
        break

for number in range(12, 15):
    if number == 14:
        print("The {} is the day of my birthday".format(number))
        continue
    else:
        print(number)

for number in range(12, 15):
    if number == 14:
        pass
    else:
        print(number)
