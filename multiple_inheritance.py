# Multiple inheritance syntax
class Item:
    def __init__(self, type):
        self.type = type

    def item_type(self):
        print("the type is {}".format(self.type))


class Print:
    def __init__(self, color):
        self.color = color

    def item_color(self):
        print("the color is {}".format(self.color))


class Skirt(Item, Print):
    def __init__(self, size, number, type, color):
        self.size = size
        self.number = number
        Item.__init__(self, type)
        Print.__init__(self, color)

    def skirt_avail(self):
        print("The skirt with {} and {} is available".format(self.size, self.number))


Blouse = Skirt("XS", 9087, "stripped", "beige")
Blouse.item_color()
Blouse.skirt_avail()
Blouse.item_type()

