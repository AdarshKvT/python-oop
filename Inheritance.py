# generalized class
class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")

    def speak(self):
        print("I dont no what to say")


# child class inheriting from parent class.
class Cat(Pet):

    # if need to add more attributes, we can simply introduce __init in the child class. And use super() method for
    # using generalized init values

    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        print("Meow")

    # defining child own show method for the color attribute
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old. I am {self.color} ")


class Dog(Pet):
    def speak(self):
        print("bark")


class Fish(Pet):
    pass


# create an instance of the pet class
p = Pet("KvT", 26)

p.show()
p.speak()

# below snippet shows child class inheriting properties of parent class method show()
c = Cat("Bill", 34, "Green")
c.show()
c.speak()

d = Dog("Jill", 24)
d.show()
d.speak()

# As there is no method for speak inside the Fish class so it uses parent method, else overriding takes place
f = Fish("Bubble", 23)
f.speak()
