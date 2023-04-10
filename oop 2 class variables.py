class Employee:
    number_of_employee = 0
    raise_amount = 1.05

    def __init__(self, first, last, salary):
        self.firstname = first
        self.lastname = last
        self.salary = salary

        Employee.number_of_employee += 1

    def full_name(self):
        return f"{self.firstname} {self.lastname}"

    def apply_raise(self):
        self.salary = int(self.salary * self.raise_amount)
        return f"salary: {self.salary} raise_amount: ^{self.raise_amount}%\n"


emp1 = Employee("srinu", "koda", 50000)
emp2 = Employee("pavan", "koda", 50000)
emp3 = Employee("sai", "koda", 50000)
Employee.raise_amount = 1.04
emp1.raise_amount = 1.07
emp3.raise_amount = 1.06
print(f"Default raise: {Employee.raise_amount}")
print(emp1.full_name())
print(emp1.apply_raise())
print(emp2.full_name())
print(emp2.apply_raise())
print(emp3.full_name())
print(emp3.apply_raise())
print(f"Total number of employees: {Employee.number_of_employee}")
