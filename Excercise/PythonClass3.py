"""
This file is about class-inheritance
also little bit about 'isinstance' 'issubclass' [introduction]
"""


class Employee:
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first.lower() + "." + last.lower() + "@email.com"

    def fullname(self):
        return f"{self.first} {self.last}"

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


class Developer(Employee):
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

        # or it can be done by this
        # Employee.__init__(self, first, last, pay)
        # self.prog_lang = prog_lang


class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print("---> ", emp.fullname())


# =======================================
# dev_1 = Employee("Jay", "Patel", 120000)
# dev_2 = Employee("Test", "User", 75000)

# print(dev_1.email)
# print(dev_2.email)

# =======================================

# dev_1 = Developer("Jay", "Patel", 120000)
# dev_2 = Developer("Test", "User", 75000)

# print(dev_1.email)
# print(dev_2.email)

# print(help(Developer))

# =======================================
# dev_1 = Developer("Jay", "Patel", 120000, "C/C++")
# dev_2 = Developer("Test", "User", 75000, "Python")

# print(dev_1.prog_lang)
# print(dev_2.prog_lang)

# =======================================

# dev_1 = Developer("Jay", "Patel", 120000, "C/C++")
# dev_2 = Developer("Test", "User", 75000, "Python")

# mgr_1 = Manager("Michale", "Scott", 90000, [dev_1])
# print(mgr_1.fullname())

# mgr_1.print_emps()
# mgr_1.add_emp(dev_2)
# mgr_1.print_emps()

# mgr_1.remove_emp(dev_2)
# mgr_1.print_emps()
# =======================================

# dev_1 = Developer("Jay", "Patel", 120000, "C/C++")
# mgr_1 = Manager("Michale", "Scott", 90000, [dev_1])

# # is mgr_1 is instance of Manager?
# print(isinstance(mgr_1, Manager))  # --> True

# # is mgr_1 is instance of Employee?
# print(isinstance(mgr_1, Employee))  # --> True

# # is mgr_1 is instance of Developer?
# print(isinstance(mgr_1, Developer))  # --> False

# =======================================

# dev_1 = Developer("Jay", "Patel", 120000, "C/C++")
# mgr_1 = Manager("Michale", "Scott", 90000, [dev_1])

# # is Developer subclass of Employee?
# print(issubclass(Developer, Employee))  # --> True

# # is Manager subclass of Employee?
# print(issubclass(Manager, Employee))  # --> True

# # is Manager subclass of Developer?
# print(issubclass(Manager, Developer))  # --> False

# =======================================
