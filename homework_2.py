class Person:
    def __init__(self, name, birth_date, occupation):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation

    def introduce(self):
        print(f"Hello, my name is {self.name}, i was born in {self.birth_date}. I work as a {self.occupation}.\n")

class Classmate(Person):
    def __init__(self, name, birth_date, occupation, group_name):
        super().__init__(name, birth_date, occupation)
        self.group_name = group_name

    def introduce(self, friend_name):
        self.friend_name = friend_name
        print(
            f"Hello, my name is {self.name}, I was born in {self.birth_date}, I am groupmate of {friend_name}. I study at {self.group_name} group. I work as a {self.occupation}.\n")


class Friend(Person):
    def __init__(self, name, birth_date, occupation, hobby):
        super().__init__(name, birth_date, occupation)
        self.hobby = hobby

    def introduce(self, friend_name):
        print(
            f"Hello, my name is {self.name}, I was born in {self.birth_date}, I am friend of {friend_name}, I work as a {self.occupation}. My hobby is {self.hobby}.\n")


friend = Friend("Elnura", "01.02.2005", "Engineering", "playing a guitar")
friend.introduce("Albina")

mate = Classmate("Aizhan", "02.11.2004", "Data Science", "BIL-202")
mate.introduce("Azamat")


