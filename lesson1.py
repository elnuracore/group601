class Car:    # creates class, better to name with bigger letter, title
    def __init__(self, color, model):   # __init__  - initializer (constructor), self - pointer in class
        self.color = color  # properties
        self.model = model

    def drive(self, location):  # method
        print(f"Car {self.model} is driving in {location}")
    def test(self):
        self.drive("Karkol")

car_honda = Car(color="red", model="Honda") # creates object
car_subaru = Car(color="silver", model="Subaru")

car_subaru.drive("Bishkek")
car_honda.drive("Osh")
car_honda.test()
print(car_honda)
print(car_subaru)
print(car_honda.color)
print(car_subaru.color)
print(car_honda.model == car_subaru.model)
print(type(car_honda))
print(type(Car))

""""Dunder methods""" # double underscore
