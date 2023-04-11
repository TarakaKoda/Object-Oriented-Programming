class Employee:
    company_name = "tcs"

    def __init__(self, first, last, salary):
        self.first_name = first
        self.last_name = last
        self.salary = salary

    @property
    def email(self):
        return f"{self.first_name.lower()}{self.last_name.lower()}@{Employee.company_name}.com"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @full_name.setter
    def full_name(self, name):
        first, last = name.split()
        self.first_name = first
        self.last_name = last

    @full_name.deleter
    def full_name(self):
        print("Deleted Name")
        self.first_name = None
        self.last_name = None


emp1 = Employee("Srinivas", "Koda", 50000)
print(emp1.email)
emp1.first_name = "pavan"
emp1.last_name = "uchiha"
print(emp1.full_name)
print(emp1.email)
emp1.full_name = "john cena"
print(emp1.full_name)
del emp1.full_name
print(emp1.full_name)