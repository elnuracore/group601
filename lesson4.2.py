# ABC abstract basic class
from abc import ABC, abstractmethod

class Animal(ABC):  # not concrete,
    @abstractmethod
    def make_sound(self): # this method always should be in subclasses, otherwise it will be error or it will give us mistake
        pass

class Dog(Animal):   # concrete
    def test(self):
        print("Dog test")
    def make_sound(self):   # make_sound should be always, otherwise it does not work , because it is in abstract class
        print("Gav - gav")

class Cat(Animal):
    def test(self):
        print("Cat test")
    def make_sound(self):
        print("Myau - myau")

puppy = Dog()
puppy.make_sound()
kitten = Cat()
kitten.make_sound()