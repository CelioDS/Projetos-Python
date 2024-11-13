class Person:
    def __init__(self, name=None, yearOld=None):
        self.name = name,
        self.yearOld = yearOld


    @classmethod
    def create_date(cls, ano,mes,dia,name):
        yearOld = 2020 - ano
        return cls(name, yearOld)

    @staticmethod
    def adult(yearOld):
        return yearOld >= 18

person = Person.create_date(1998,3,21,"guilherme")

person1 = Person.adult(18)
person2 = Person.adult(17)
print(person.name)
print(person1)
print(person2)