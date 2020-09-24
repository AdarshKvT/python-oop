class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        # print(name)

    # below method will return us the attribute value of the object

    # getter
    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    # setter
    # set the different  age
    def set_age(self, age):
        self.age = age


d = Dog("tyson", 12)
d.set_age(25)
# d2 = Dog("Delta", 14)
# d3 = Dog("Charlie", 10)

print(d.get_age())
# print(d.get_name())
# print(d2.get_name())

# print(d.name)
# print(d2.name)
# print(d3.name)
