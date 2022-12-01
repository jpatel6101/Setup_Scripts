"""
This file is about classes & instances, class-variables & instance-variables 
"""


class Employee:

    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = (self.first).lower() + "." + self.last.lower() + "@email.com"
        Employee.num_of_emps += 1

    def fullname(self):
        return self.first + " " + self.last

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


print(Employee.num_of_emps)
emp1 = Employee("John", "Doe", 50000)
emp2 = Employee("Test", "User", 6000)
print(Employee.num_of_emps)

# print(emp1.fullname())
# print(emp1.email)

print(emp1.pay)
emp1.apply_raise()
print(emp1.pay)
