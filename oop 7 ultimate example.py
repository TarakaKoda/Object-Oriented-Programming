class Employee:
    company_name = "meta"
    no_of_emp = 0
    raise_amount = 1.05

    def __init__(self, first, last, salary):
        self.first_name = first
        self.last_name = last
        self.salary = salary
        Employee.no_of_emp += 1

    @property
    def emp_email(self):
        return f"{self.first_name.lower()}.{self.last_name.lower()}@{Employee.company_name}.com"

    @property
    def emp_full_name(self):
        return f"{self.first_name} {self.last_name}"

    @emp_full_name.setter
    def emp_full_name(self,name):
        first, last = name.split()
        self.first_name = first
        self.last_name = last

    @emp_full_name.deleter
    def emp_full_name(self):
        print("Deleted Name")
        self.first_name = None
        self.last_name = None

    def full_details(self):
        return f"Employee Name: {self.first_name} {self.last_name}\nSalary: {self.salary}\nEmail Id: {Employee.emp_email}"

    def apply_raise(self):
        self.salary = int(float(self.salary) * self.raise_amount)
        return f"Salary: {self.salary} ^{self.raise_amount}%\n"

    @classmethod
    def change_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, details):
        first, last, salary = details.split("-")
        return cls(first, last, salary)

    @staticmethod
    def is_weekday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        else:
            return True


class Developer(Employee):
    def __init__(self, first, last, salary, prog_lang):
        super().__init__(first, last, salary)
        self.programming_language = prog_lang

    def __repr__(self):
        return f'{Developer.__name__}("{self.first_name}", "{self.last_name}", {self.salary}, "{self.programming_language}")'


class Manager(Employee):
    def __init__(self, first, last, salary, emp_list=None):
        super().__init__(first, last, salary)
        if emp_list is None:
            self.emp_list = []
        else:
            self.emp_list = emp_list

    def add_employee(self, emp):
        if emp not in self.emp_list:
            self.emp_list.append(emp)
        return f"{emp} is successfully added"

    def remove_employee(self, emp):
        if emp in self.emp_list:
            self.emp_list.remove(emp)
        return f"{emp} is successfully removed"

    def list_of_employee(self):
        for emp in self.emp_list:
            print(emp.full_details())
            print(emp.apply_raise())

    def __repr__(self):
        return f'{Manager.__name__}("{self.first_name}", "{self.last_name}", {self.salary})'

    def __str__(self):
        return f'class {Manager.__name__} methods are: "add_employee", "remove_employee", "list_of_employee"'

    def __add__(self, other):
        return self.salary + other.salary


emp1 = Employee("Srinivas", "Koda", 50000)
emp2 = Employee("Pavan", "koda", 50000)
emp1.raise_amount = 1.07
Employee.change_raise_amount(1.07)
# print(emp2.apply_raise())
emp3 = Employee.from_string("Naruto-Uzumaki-50000")
# print(emp3.full_details())
emp3.raise_amount = 1.09
# print(emp3.apply_raise())

import datetime

today = datetime.date(2030, 4, 12)
# print(Employee.is_weekday(today))

dev1 = Developer("Sasuke", "Uchiha", 60000, "Python")
dev2 = Developer("Itachi", "Uchiha", 60000, "Java")
# print(dev1.apply_raise())
dev2.raise_amount = 1.09
# print(dev2.apply_raise())
mrg1 = Manager("Kakashi", "Hatake", 90000, [emp2])
# mrg1.add_employee(dev1)
# mrg1.add_employee(dev2)
# mrg1.add_employee(emp3)
# mrg1.list_of_employee()
# print(mrg1)
# print(dev1)
# print(mrg1 + dev1)
print(emp1.emp_full_name)
emp1.emp_full_name = "sai koda"
print(emp1.emp_full_name)
del emp1.emp_full_name
print(emp1.emp_full_name)