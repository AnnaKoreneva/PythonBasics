"""
- Python classes goal to group data and information like variables and functions into a single organized unit
- Classes allow to share info with other class and parts of the python program
- Classes have features like inheritance which allow us to borrow from one class and use elements of that class to create
another class.
- Python also allows for multiple inheritance which allows a class to inherit attributes from multiple classes.
- All classes are objects
- The statements or information inside a class are usually functions, but a class can also contain class variables that
are specific to the class and usable throughout the entire class.
- There are also variables called instance variables and those variables are specific to any Objects that are created by
the class.
- The __init__ method allows every instance of a class to be created or initialized with specific parameters
pre-determined at the creation of that Object.
- The self variable in Python represents an instance of a class, and specifically it references the instance of the
class that has been created.
We use self in order to make available all the attributes to the methods throughout the class.
"""


class Person:
    def __init__(self, first_name, last_name, health_score, friend):
        self.first_name = first_name
        self.last_name = last_name
        self.health_score = health_score
        self.friend = friend

    def introduction(self):
        print("My name is {} and last name is {}". format(self.first_name, self.last_name))

    def health_state(self):
        if self.health_score == 100:
            print("The {}{} is a very healthy person. Good job".format(self.first_name, self.last_name))
        elif self.health_score >=80:
            print("The {}{} you need to pay attention to you health.".format(self.first_name, self.last_name))
        elif self.health_score >= 50:
            print("The {}{} you need to visit family doctor.".format(self.first_name, self.last_name))
        else:
            print("The {}{} you need to visit family doctor RIGHT NOW.".format(self.first_name, self.last_name))

    def friend_state(self):
        if self.friend:
            print("The {}{} is my friend.".format(self.first_name, self.last_name))
        else:
            print("I don't know {}{}".format(self.first_name, self.last_name))


Anna = Person("Anna", "Koreneva", 99, True)
Anna.introduction()
Anna.health_state()
Anna.friend_state()
