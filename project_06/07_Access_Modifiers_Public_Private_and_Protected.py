# Create a class Employee with:

# a public variable name,
# a protected variable _salary, and
# a private variable __ssn.
# Try accessing all three variables from an object of the class and document what happens.


class Employee:
    def __init__(self):
        self.employee_name = "Babar Azam"
        self._employee_age = 30
        self.__employee_profession = "Cricketer"
        
emp = Employee()

print(f"The name of our Employee is: {emp.employee_name}")
print(f"The age of our Employee is: {emp._employee_age}")
# print(f"The profession of our Employee is: {emp.__employee_profession}")   Private will give you error


print(emp._Employee__employee_profession)
