class Person:
    number_of_people = 0

    def __init__(self, name):
        print("__init__ initiated")
        self.name = name

        print("calling add_person()")
        Person.add_person()

    @classmethod
    def num_of_people(cls):
        print("initiating num_of_person()")
        return cls.number_of_people

    @classmethod
    def add_person(cls):
        print("add_person(cls)")
        cls.number_of_people += 1


# create an object of person
p1 = Person("KvT")

# creating another instance
p2 = Person("Shin")

# accessing the class method directly
print(Person.num_of_people())
