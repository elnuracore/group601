from lesson1 import car_honda
class Car:
    def __init__(self, color, model, value):
        self.color = color
        self.model = model
        self.__fined = False
        self.__value = value
    def drive(self, location):
        print(f"Car {self.model} is driving in {location}")
    def test(self):
        self.drive("Karakol")

    # def get_fined(self):   # when we wanna use private outside of the class
    #     return self.__fined
    #
    # def set_fined(self, value):
    #     self.__fined = value  # when we wanna
    @property   # decorators in python
    def fined(self):
        return self.__fined
    @fined.setter
    def fined(self, val):
        self.__fined = val
    def set_max(self, value):
        if type(value) != bool:
            raise TypeError("fined must be boolean")
        self.__max_speed = value
# child class, subclass, inheritance
class Bus(Car):
    def __init__(self, color, model, seats):
        super().__init__(color, model)
        self.seats = seats

    def test_bus(self):
        # super().drive(location)
        print(f"Bus test {self.model}")
    def drive(self, location):
        print(f"Bus {self.model} is driving in {location}")

bus_1 = Bus("green", "Isuzu", 40)
print(bus_1.seats)
print(bus_1.color)
bus_1.drive("Bishkek")
# print(bus_1._fined)  # _ means protected, it is not recommended
# bus_1._test()
print(bus_1.get_fined)  # __ means protected, it is not true and it gives error

# car1.set_max(0) # error
print(car1.fined)
car1.fined = True
print(car1.fined)