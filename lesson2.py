# Parent, super class
class Car:
    def __init__(self, color, model):
        self.color = color
        self.model = model
    def drive(self, location):
        print(f"Car {self.model} is driving in {location}")
    def test(self):
        self.drive("Karkol")

# child class, subclass, inheritance
class Bus(Car):
    def __init__(self, color, model, seats):
        super().__init__(color, model)
        self.seats = seats

    def test_bus(self):
        super().drive(location)
        print(f"Bus test {self.model}")
    def drive(self, location):
        print(f"Bus {self.model} is driving in {location}")

bus_1 = Bus("green", "Isuzu", 30)
print(bus_1.color)
bus_1.drive("Bishkek")
bus_1.test_bus()
print(bus_1.seats)
