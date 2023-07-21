class Vehicle:
    def __init__(self, body_type):
        self.body_type = body_type

    def drive_speed(self, speed):
        self.mode = "driving"
        self.speed = speed


class Car(Vehicle):
    def __init__(self, engine_type):
        super().__init__("Car")
        self.engine_type = engine_type
        self.wheels = 4
        self.doors = 5


class Motorcycle(Vehicle):
    def __init__(self, engine_type, has_side_car):
        super().__init__("Motorcycle")
        self.engine_type = engine_type
        self.doors = 0
        if has_side_car:
            self.wheels = 3
        else:
            self.wheels = 2


car_1 = Car("electric")
car_2 = Car("gas")
motorcycle = Motorcycle("electric", False)
car_1.speed = 60

print("I have an {} car with number of {} and {}. It can drive with the speed {}".format(car_1.engine_type, car_1.doors,
                                                                                         car_1.wheels, car_1.speed))
