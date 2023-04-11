class Employee:
    company_name = "tcs"
    raise_amount = 1.05

    def __init__(self, first, last, salary):
        self.first_name = first
        self.last_name = last
        self.salary = salary
        self.email = f"{first}{last}@{Employee.company_name}.com"

    def full_details(self):
        return f"Employee Name: {self.first_name} {self.last_name}\nSalary: {self.salary}\nEmail Id: {self.email}"

    def apply_raise(self):
        self.salary = int(self.salary * self.raise_amount)
        return f"annual salary: {self.salary} and raise amount: ^{self.raise_amount}"

    def __repr__(self):
        return f'{Employee}("{self.first_name}", "{self.last_name}", "{self.salary}")'

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.email}"

    def __add__(self, other):
        return self.salary + other.salary

    def __sub__(self, other):
        return self.salary - other.salary


emp1 = Employee("srinivas", "koda", 50000)
emp2 = Employee("pavan", "koda", 50000)
print(emp1.apply_raise())
# emp2.raise_amount = 1.06
# print(emp2.apply_raise())
print(emp2)
print(emp2)
print(emp1 + emp2)
print(emp1 - emp2)