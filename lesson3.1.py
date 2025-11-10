# polymarphism
from lesson1 import car_honda


class Car:
    def __init__(self, color, model):
        self.color = color
        self.model = model
    def drive(self, location):
        print(f"Car {self.model} is driving in {location}")
    def test(self):
        self.drive("Karakol")

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

class Truck(Car):
    pass
car_honda = Car("white", "Honda")

bus_1 = Bus("green", "Isuzu", 30)
print(bus_1.color)
bus_1.drive("Bishkek")
bus_1.test_bus()
print(bus_1.seats)
truck_man = Truck("red", "Man")

vehicles = [car_honda, bus_1, truck_man]
for v in vehicles:
    v.drive(location="Karakol")


