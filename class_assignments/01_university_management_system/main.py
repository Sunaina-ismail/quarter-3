# Base Class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getName(self):
        return self.name

# Student class inherits from Person
class Student(Person):
    def __init__(self, name, age, rollNumber):
        super().__init__(name, age)
        self.rollNumber = rollNumber
        self.courses = []

    def registerForCourses(self, course):
        self.courses.append(course)
        course.addStudent(self)

# Instructor class inherits from Person
class Instructor(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary
        self.courses = []

    def assignCourse(self, course):
        self.courses.append(course)
        course.setInstructor(self)

# Course class
class Course:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.students = []
        self.instructor = None

    def addStudent(self, student):
        self.students.append(student)

    def setInstructor(self, instructor):
        self.instructor = instructor

# Department class
class Department:
    def __init__(self, name):
        self.name = name
        self.courses = []

    def addCourse(self, course):
        self.courses.append(course)


department = Department("Computer Science")
course = Course(101, "Introduction to TypeScript")
department.addCourse(course)

instructor = Instructor("Sir Hamzah Syed", 45, 120000.0)
instructor.assignCourse(course)

student = Student("Rayyan", 20, "CS123")
student.registerForCourses(course)



# Output
print("\n===== University Management Info =====")
print(f"Department: {department.name}")
print(f"Course: {course.name} (ID: {course.id})")
print(f"Instructor: {course.instructor.getName()} | Age: {course.instructor.age}")
print(f"Students Enrolled in {course.name}:")
for s in course.students:
    print(f"- {s.getName()} (Roll No: {s.rollNumber})")
