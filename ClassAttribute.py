class Person:
    number_of_people = 0

    def __init__(self, name):
        self.name = name

        # number of person created
        Person.number_of_people += 1


# create an object of person
p1 = Person("KvT")

# creating another instance
p2 = Person("Shin")

p3 = Person("hokage")

print(Person.number_of_people)
Person.number_of_people = 8
print(Person.number_of_people)
