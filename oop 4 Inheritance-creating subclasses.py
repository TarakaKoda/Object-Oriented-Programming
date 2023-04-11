class Employee:
    no_of_emp = 0
    raise_amount = 1.05
    company_name = "tcs"

    def __init__(self, first, last, salary):
        self.first_name = first
        self.last_name = last
        self.salary = salary
        self.email = f"{first.lower()}{last.lower()}@{Employee.company_name}.com"
        Employee.no_of_emp += 1

    def full_details(self):
        return f"{Employee.__name__} Name: {self.first_name} {self.last_name}\nSalary: {self.salary}\nEmail Id: {self.email}\n"

    def apply_raise(self, grade):
        if grade.upper() == "A":
            self.raise_amount = Employee.raise_amount + 0.02
            self.salary = int(self.salary * self.raise_amount)
            return f"Congratulation!! You have acquired '{grade.upper()}', Updated salary: {self.salary} ^{self.raise_amount}%"
        elif grade.upper() == "B":
            self.salary = int(self.salary * self.raise_amount)
            return f"Congratulation!! You have acquired '{grade.upper()}', Updated salary: {self.salary} ^{self.raise_amount}%"
        else:
            return f"Please enter the grade as 'A' or 'B'"

    @classmethod
    def change_raise_amount(cls, amount):
        cls.raise_amount = amount
        return cls.raise_amount

    @classmethod
    def from_string(cls, details):
        first, last, salary = details.split("-")
        return cls(first, last, salary)

    @staticmethod
    def is_weekend(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        else:
            return True


class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, salary, prog_lang):
        super().__init__(first, last, salary)
        self.prog_language = prog_lang


class Manager(Employee):
    def __init__(self,first, last, salary,employee=None):
        super().__init__(first, last, salary)
        if employee is None:
            self.employees_list = []
        else:
            self.employees_list = employee

    def add_employees(self,emp):
        if emp not in self.employees_list:
            self.employees_list.append(emp)

    def remove_employee(self,emp):
        if emp in self.employees_list:
            self.employees_list.remove(emp)

    def print_employees_list(self):
        for emp in self.employees_list:
            print(emp.full_details())


emp1 = Employee("Srinivas", "Koda", 50000)
emp2 = Employee("Pavan", "Koda", 50000)

# print(emp1.full_details())
# print(emp2.full_details())

dev1 = Developer("Naruto", "Uzumaki", 70000, "Python")
dev2 = Developer("Sasuke", "Uchiha", 60000, "Java")

magr1 = Manager("Kakshi", "Hatake",90000,[dev1])
# magr1.add_employees(dev1)
magr1.remove_employee(dev2)
magr1.add_employees(dev2)
magr1.add_employees(magr1)
magr1.print_employees_list()

print(isinstance(magr1,Developer))
print(issubclass(Developer, Manager))
print(Employee.no_of_emp)