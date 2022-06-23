class Person(object):
    population = 50

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def get_population(cls):
        return cls.population

    @staticmethod
    def is_adult(age):
        return age >= 18

    def display(self):
        print(f"{self.name} is {self.age} years old")


if __name__ == "__main__":
    print(Person.get_population())
    print(Person.is_adult(6))
    new_person = Person('ishwor', 24)
