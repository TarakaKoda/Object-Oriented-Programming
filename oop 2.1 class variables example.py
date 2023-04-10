class Employee:
    number_of_employee = 0
    raise_amount = 1.05
    company_name = "tcs"
    minimum_salary = 50000
    total_number_of_raise = 0

    def __init__(self, first, last, salary):
        self.first_name = first
        self.last_name = last
        self.salary = salary
        self.email = f"{first}{last}@{Employee.company_name}.com"
        Employee.number_of_employee += 1

    def full_details(self):
        return f"EMPLOYEE NAME: {self.first_name} {self.last_name}\nSALARY: {self.salary}\nEMAIL ID: {self.email}"

    def apply_raise(self):
        if self.salary >= self.minimum_salary:
            self.salary = int(self.salary * self.raise_amount)
            Employee.total_number_of_raise += 1
            return f"TOTAL SALARY: {self.salary}, RAISED AMOUNT BY: ^{self.raise_amount}%\n"
        else:
            return f"sorry!! your salary: {self.salary} is under the basic requirement ie.. {self.minimum_salary}, better luck next time.\n"


emp1 = Employee("naruto", "uzumaki", 70000)
emp2 = Employee("sasuke", "uchiha", 70000)
emp3 = Employee("sakura", "haruno", 60000)
emp1.raise_amount = 1.05
emp2.raise_amount = 1.04
emp1.minimum_salary = 70000
emp2.minimum_salary = 60000
emp3.minimum_salary = 70000
print(emp1.full_details())
print(emp1.apply_raise())
print(emp2.full_details())
print(emp2.apply_raise())
print(emp3.full_details())
print(emp3.apply_raise())
print(f"The Total Number of Employees Present in the Organization is: {Employee.number_of_employee}\nTotal Number of raises: {Employee.total_number_of_raise}")
