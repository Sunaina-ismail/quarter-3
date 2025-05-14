# 🎓 University Management System – OOP Assignment
**Assignment by:** Sir Hamzah Syed.
**Author:** Sunaina Ismail.

This project is a simple University Management System built using Python and Object-Oriented Programming concepts. It was developed as part of a class assignment to implement inheritance and real-world relationships using OOP.

---

## 📁 Project Overview

The system models a basic structure of a university with the following entities:

- **Person** (Base Class)
- **Student** (inherits from Person)
- **Instructor** (inherits from Person)
- **Course**
- **Department**

---

## 🧱 Classes and Their Responsibilities

### 1. `Person`
- Base class for both students and instructors.
- Attributes: `name`, `age`
- Method: `getName()`

### 2. `Student` (inherits from `Person`)
- Additional Attribute: `rollNumber`
- Method: `registerForCourses(course)`
- Can register for multiple courses.

### 3. `Instructor` (inherits from `Person`)
- Additional Attribute: `salary`
- Method: `assignCourse(course)`
- Can be assigned to multiple courses.

### 4. `Course`
- Attributes: `id`, `name`, `students`, `instructor`
- Methods: `addStudent(student)`, `setInstructor(instructor)`
- Maintains a list of enrolled students and assigned instructor.

### 5. `Department`
- Attributes: `name`, `courses`
- Method: `addCourse(course)`
- Represents a department that offers multiple courses.

---

## 🛠️ What I Implemented

- Created a `Department` named **Computer Science**.
- Created a `Course` named **Introduction to Programming** with ID `101`.
- Created an `Instructor` named **Dr. Ahmed** (age: 45, salary: 120000.0).
- Assigned the instructor to the course.
- Created a `Student` named **Ayesha** (age: 20, roll no: CS123).
- Registered the student in the course.

---

## ✅ Sample Output

```
===== University Management Info =====
Department: Computer Science
Course: Introduction to Programming (ID: 101)
Instructor: Dr. Ahmed | Age: 45
Students Enrolled in Introduction to Programming:
```


---

## 💡 Concepts Practiced

- Object-Oriented Programming
- Inheritance
- Class relationships and composition
- Clean class structure and method usage

---

## 🖥️ Technologies Used

- Python 3
- OOP Principles

---

## 📌 Notes

This assignment helped me understand how to:
- Use inheritance in a real-world scenario.
- Establish relationships between multiple classes.
- Apply clean and reusable object-oriented design patterns.



