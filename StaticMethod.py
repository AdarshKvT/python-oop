class Math:

    @staticmethod
    def add(x, y):
        addition = x + y
        return addition

    @staticmethod
    def pr():
        print("run")


print(Math.add(4, 5))

# calling method without passing any argument
Math.pr()