"""
This file is about @classmethod && @staticmethod

@classmethod takes class (for ex. cls) as default argument.
while returning we need to mention cls 

@staticmethod does not takes any class name as default, we don't need to pass class
where we don't need to anything with class then we use static method
check below example for ref...
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

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split("-")
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


# ==========================================================

# emp1 = Employee("John", "Doe", 50000)
# emp2 = Employee("Test", "User", 6000)

# Employee.set_raise_amt(1.05)
# emp1.set_raise_amt(1.05)

# print(Employee.raise_amount)
# print(emp1.raise_amount)
# print(emp2.raise_amount)

# ===========================================================

emp1 = Employee("John", "Doe", 50000)
emp2 = Employee("Test", "User", 6000)

emp_str_1 = "michale-scott-85000"
emp_str_2 = "dwight-schrute-80000"
emp_str_3 = "pam-besley-70000"

# first, last, pay = emp_str_1.split("-")
# new_emp_1 = Employee(first, last, pay)
# print(new_emp_1.fullname())
# print(new_emp_1.email)

new_emp_1 = Employee.from_string(emp_str_1)
print(new_emp_1.fullname())
print(new_emp_1.email)
# ===========================================================

# checking static method
import datetime

my_date_1 = datetime.date(2022, 3, 19)  # saturday
my_date_2 = datetime.date(2022, 3, 18)  # friday
print(Employee.is_workday(my_date_1))  # --> return false
print(Employee.is_workday(my_date_2))  # --> return true
