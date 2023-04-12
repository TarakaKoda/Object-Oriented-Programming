from abc import ABC, abstractmethod


class Employee(ABC):
    def __init__(self,first, last, salary):
        self.first_name = first
        self.last_name = last
        self.salary = salary

    @abstractmethod
    def full_details(self):
        return f"{self.salary}, {self.first_name} {self.last_name}"


class Developer(Employee):
    def __init__(self,first,last,salary,prog):
        super().__init__(first, last, salary)
        self.programming_language = prog

    def full_details(self):
        return f"Developer Nanme: {self.first_name} {self.last_name}\nSalary: {self.salary}\nEmail Id: {self.first_name.lower()}{self.last_name.lower()}@gmail.com"


class Manager(Employee):
    def __init__(self, first, last, salary, emp=None):
        super().__init__(first, last, salary)
        if emp is None:
            self.emp_list = []
        else:
            self.emp_list = emp

    def add_emp(self,emp):
        if emp not in self.emp_list:
            self.emp_list.append(emp)
            return f"Employee: {emp} is added."
        else:
            return f"Employee: {emp} already exists."

    def remove_emp(self, emp):
        if emp in self.emp_list:
            self.emp_list.remove(emp)
            return f"Employee: {emp} is deleted."
        else:
            return f"Employee: {emp} does not exists."

    def full_details(self):
        return f"Manager Name: {self.first_name} {self.last_name}\nSalary: {self.salary}\nNo.of Employees Working under {self.first_name} {self.last_name}: {', '.join([x.first_name for x in self.emp_list])}"


# emp1 = Employee("srinu", "koda", 50000)
# emp2 = Employee("pavan", "koda", 50000)
dev1 = Developer("naruto", "uzumaki", 60000, "python")
dev2 = Developer("sasuke", "uchiha", 60000, "java")
magr1 = Manager("kakashi", "hatake", 70000)
# magr1.add_empl(emp2)
magr1.add_emp(dev1)
magr1.add_emp(dev2)
print(dev1.full_details())
print(magr1.full_details())


