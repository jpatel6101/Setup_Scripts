"""
This file is about Special Methods (Magic-Method && Dunder-Method)
also about operator overloading
"""


class Employee:
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first.lower() + "." + last.lower() + "@email.com"

    def fullname(self):
        return self.first + " " + self.last

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def __repr__(self):
        pass

    def __str__(self):
        pass


emp_1 = Employee("John", "Doe", 50000)
emp_2 = Employee("Test", "User", 6000)

print(emp_1)

repr(emp_1)
str(emp_1)
