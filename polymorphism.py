# In simple words it is method overriding
# Polymorphism occurs when we want to allow the child class to have a method with the same name and a similar
# implementation as the parent class, and we wish for that method you override the parent class method.
class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def intro(self):
        print("My Name is {} {} and I am {} years old".format(self.first_name, self.last_name, self.age))

class Employee(Person):
    def __init__(self, position, first_name, last_name, age):
        self.position = position
        Person.__init__(self, first_name, last_name, age)

    def intro(self):
        print("My Name is {} {} and I am {} years old. I am a {} at company".format(self.first_name, self.last_name,
                                                                                    self.age, self.position))


Anna = Employee("QA", "Anna", "Koreneva", "31")
Anna.intro()

Anna = Person("Anna", "Koreneva", "31")
Anna.intro()
