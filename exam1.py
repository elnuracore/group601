class Animal:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        if age >= 0:
            self.__age = age
        else:
            print("Возраст не может быть отрицательным")

    def make_sound(self):
        print("Животное издаёт звук")


class Dog(Animal):
    def make_sound(self):
        print("Гав-гав")


class Cat(Animal):
    def make_sound(self):
        print("Мяу-мяу")


dog = Dog("Бим", 3)
cat = Cat("Барсик", 2)

dog.make_sound()
cat.make_sound()

print("Имя собаки:", dog.get_name(), "| Возраст:", dog.get_age())
print("Имя кота:", cat.get_name(), "| Возраст:", cat.get_age())

dog.set_name("Шарик")
dog.set_age(5)

cat.set_name("Снежок")
cat.set_age(4)

print(dog.get_name(), "| Возраст:", dog.get_age())
print(cat.get_name(), "| Возраст:", cat.get_age())
