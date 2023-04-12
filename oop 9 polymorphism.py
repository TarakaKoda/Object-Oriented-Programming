# Polymorphism:

# Polymorphism is the process of using a single interface to represent multiple types of objects. In Python,
# this is typically achieved through method overriding and method overloading.

class Employee:
    def __init__(self, first, last, salary):
        self.first_name = first
        self.last_name = last
        self.salary = salary

    def email(self):
        pass


class Developer(Employee):
    def __init__(self, first, last, salary, prog_lang):
        super().__init__(first, last, salary)
        self.programming_language = prog_lang

    def email(self):
        return f"{self.first_name}{self.last_name}@gamil.com"


class Manager(Employee):
    def __init__(self, first, last, salary, emp_list=None):
        super().__init__(first, last, salary)
        if emp_list is None:
            self.emps_list = []
        else:
            self.emps_list = emp_list

    def email(self):
        return f"{self.first_name}{self.last_name}@gamil.com"


def employee_email(empl):
    return empl.email()


dev1 = Developer("srinu", "koda", 50000, "Python")
magr1 = Manager("pavan", "koda", 90000)

print(employee_email(dev1))
print(employee_email(magr1))