# Python Object-Oriented Programming
class Employee:
    company_name = "tcs"

    def __init__(self,First_name, Last_name, pay):
        self.First_name = First_name
        self.Last_name = Last_name
        self.pay = pay
        self.Email = f"{First_name}{Last_name}@{Employee.company_name}.com"

    def full_details(self,no_number):
        return f"employee name: {self.First_name} {self.Last_name}\nsalary: {self.pay}\ncontact no: {no_number}\nemail_id: {self.Email}\n"

    def is_available(self,status):
        if status is False:
            return f"{self.First_name} {self.Last_name} is not available "
        else:
            return f"{self.First_name} {self.Last_name} is available"


emp1 = Employee("taraka","satya",50000)
emp2 = Employee("naga", "pavan", 750000)
# print(Employee.full_details(emp1,9398803998))
# these both are same
print(emp1.full_details(9398803998))
print(emp2.full_details(8919623820))
emp3 = Employee("sai", "koda", 40000)
print(emp3.full_details(9666428769))


# This is manually entering the details of employee
# Employee.company_name = "infosys"
# Employee.firstname = "sai"
# Employee.lastname = "koda"
# Employee.email = f"{Employee.firstname}{Employee.lastname}@{Employee.company_name}.com"
#
# print(Employee.lastname)
# print(Employee.email)
print(emp1.is_available(True))