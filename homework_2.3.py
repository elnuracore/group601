class Person:
    def __init__(self, name, birth_date, occupation):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation

    def introduce(self):
        print(f"\nHello, my name is {self.name}, i was born in {self.birth_date}. I work as a {self.occupation}.\n")


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


class BestFriend(Friend):
    def __init__(sefl, name, birth_date, occupation, hobby):
        super().__init__(name, birth_date, occupation, hobby)

    def introduce(self, shared_memory):
        self.shared_memory = shared_memory
        super().introduce("Altynai")
        print(f"We walked in the {self.shared_memory} city.")


person1 = Person("Aliya", "06.07.2002", "Biology teacher")
friend1 = Friend("Elnura", "01.02.2005", "Engineering", "playing a guitar")
mate1 = Classmate("Aizhan", "02.11.2004", "Data Science", "BIL-202")
bestfriend1 = BestFriend("Ainura", "01.05.2008", "Teacher", "Volleyball")
bestfriend1.introduce("Stuttgart")

groups = [person1, mate1, friend1]

for obj in groups:
    if isinstance(obj, Person) and not isinstance(obj, (Classmate, Friend)):
        obj.introduce()
    else:
        obj.introduce("Adina")
