""""Multiple Inheritance"""

# class Swimm:
#     def move(self):
#         return f"swimming"
#
# class Flyable:
#     def move(self):
#         return f"flying"
#     pass
#
# class Animal:
#     def move(self):
#         return f"moving"
#     pass
#
# class Duck(Flyable, Swimm, Animal):
#     def move(self):
#         return "Can swim, fly and move"
#
# donald_duck = Duck()
# print(donald_duck.move())
# print(Duck.__mro__)


class A:
    def action(self):
        return 'A'
class B(A):
    def action(self):s   return 'B'
class C(A):cl

    def action(self):

class D(A, B):
    def action(self):
return 'D'


