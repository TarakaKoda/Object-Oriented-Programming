# Python oop 3 Regular methods, Class methods, static methods.

# Regular methods: These are the most common type of methods in a class. Regular methods are defined inside a class and
# operate on an instance of that class. They can access and modify instance variables, and they are invoked using an
# instance of the class.

# Class methods: Class methods are methods that operate on the class itself rather than on an instance of the class.
# They are defined using the @classmethod decorator and take the class as their first parameter (usually named cls).
# Class methods can be used to create alternate constructors, manipulate class-level data, and so on.

# Static methods: Static methods are methods that do not operate on the class or on any instance of the class.
# They are defined using the @staticmethod decorator and do not take any special first parameter.
# Static methods are often used for utility functions that are related to the class but do not depend on any class
# or instance data.

class Employee:
    raise_amount = 1.05
    company_name = "tcs"
    total_number_of_employees = 0

    def __init__(self, first, last, salary):
        self.first_name = first
        self.last_name = last
        self.salary = salary
        self.email = f"{first}{last}@{Employee.company_name}.com"
        Employee.total_number_of_employees += 1

    def full_details(self):
        return f"EMPLOYEE NAME: {self.last_name} {self.last_name}\nSALARY: {self.salary}\nEMAIL ID: {self.email}\n"

    def annual_raise(self):
        self.salary = int(self.salary * self.raise_amount)
        return f"Raised Amount: {self.raise_amount}% Total Salary: {self.salary}"

    @classmethod
    def set_raise_method(cls, amount):
        cls.raise_amount = amount
        return cls.raise_amount

    @classmethod
    def from_string(cls, employee_string):
        first, last, salary = employee_string.split("-")
        return cls(first, last, salary)

    @staticmethod
    def check_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            print(day)
            return False
        else:
            return True


emp1 = Employee("Eren", "Yeager", 50000)
emp2 = Employee("Mikasa", "ackerman", 50000)

emp1.set_raise_method(1.06)

print(emp1.annual_raise())
print(emp2.annual_raise())
print(f"Total number of employees: {Employee.total_number_of_employees}")
emp_1 = Employee.from_string("srinu-koda-50000")
print(emp_1.salary)
import datetime

my_date = datetime.date(2023, 4, 11)
print(Employee.check_workday(my_date))
