import datetime


class Age:
    def __init__(self, birth_date):
        self.__birth_date = birth_date

    @property
    def getter(self):
        return (datetime.datetime.strptime(self.__birth_date, "%d-%m-%Y"))

    @getter.setter
    def getter(self, value):
        self.__birth_date = value


a = Age("01-02-2005")
x = (datetime.datetime.today() - a.getter).days // 365
print(f"{x} years old")



