class Car:
    cars_total = 0 # it is recommended to write above the methods
    def __init__(self, color, model, speed):
        self.color = color
        self.model = model
        self.speed = speed
        Car.cars_total += 1 # it adds whenever I create objects

    @staticmethod
    def validate_speed(speed):   # static method - it does not use parameters, methods, attributes, this function can be used outside of the class
        if speed < 0: # it is useful because to be organized
            raise ValueError("speed can not be negative")
        return True



    @classmethod   #
    def create(cls, color, model, speed):  # this is method
        if Car.validate_speed(speed): # or cls.validate_speed(speed)
            new_car = Car(color, model) # instead of Car, I can write new_car = cls(color, model), cls - is the link to own class
            return new_car

    @classmethod
    def get_cars_total(cls):
        return cls.cars_total

car_mazda = Car.create("red", "Mazda", 100)
car_1 = Car.create("blue", "Honda", -100)
print(car_mazda.color)
print(Car.cars_total)