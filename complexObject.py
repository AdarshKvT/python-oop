class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade  # 0-100

    def get_grade(self):
        print("self.grade: ",  self.grade)
        return self.grade


class Course:
    def __init__(self, course_name, max_students):
        self.course_name = course_name
        self.max_students = max_students
        self.students = []

    def add_student(self, student):
        print("enrolling student length: ", len(self.students))
        print("max student allowed: ", self.max_students)

        if len(self.students) < self.max_students:
            self.students.append(student)
            message = "Students are enrolled successfully"
            return message
        else:
            message = "Cannot enroll students. Limited seat available ", self.max_students
        return message

    def get_average_grade(self):
        value = 0
        for students in self.students:
            value += students.get_grade()
            print("Value:", value)
        return value / len(self.students)


# creating students objects

s1 = Student("KvT", 26, 96)
s2 = Student("Shin", 25, 75)
s3 = Student("Mahi", 24, 60)

# creating course for students
course = Course("Science", 4)
course.add_student(s1)
course.add_student(s2)
course.add_student(s3)

print(course.add_student(s3))
print(course.get_average_grade())
