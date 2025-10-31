class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
        self.higher_education = higher_education
    def introduce(self):
        print(f"{self.name} was born on {self.birth_date}. \nHe/She works as a {self.occupation}. \nHe/She studies at {self.higher_education} university.\n")

a1 = Person(name='Elnura', birth_date="01.02", occupation="teacher", higher_education='Manas')
a2 = Person(name='Aizhan', birth_date="10.12", occupation="waitress", higher_education='KRSU')
a1.introduce()
a2.introduce()



