class Dog:

    def add_one(self, x):
        return x + 1

    def bark(self):
        print("bark")

    def eat(self):
        print("eat")

    def sleep(self):
        print("slepp")


# creating and object derived from class dog
d = Dog()

# calling the method bark of the class dog
d.bark()
print(d)

add = d.add_one(5)
print(add)
