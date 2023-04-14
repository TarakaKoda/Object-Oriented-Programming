class Employee:
    company_name = "tcs"
    raise_amount = 1.05
    all = []

    def __init__(self, first: str, last: str, salary: float):
        # Run validation for the received attributes.
        assert salary >= 0, f"Salary '{salary}' should be greater then zero"

        # Assign to self objects
        self.first_name = first
        self.last_name = last
        self.salary = salary
        self.full_name = f"{self.first_name} {self.last_name}"
        self.email = f"{self.first_name.lower()}{self.last_name.lower()}@{Employee.company_name}.com"
        Employee.all.append(self)

    def full_details(self):
        return f"{self.__class__.__name__}: {self.first_name}\nSalary: {self.salary}\n{self.__class__.__name__} Email Id: {self.email}"

    @property
    def monthly_salary(self):
        actual_ctc = self.apply_tax()
        return int(actual_ctc / 13.7)

    def apply_raise(self):
        print(f"In-hand salary per month: {self.monthly_salary:,.2f}")
        self.salary = int(self.salary * self.raise_amount)
        return f"{self.__class__.__name__} {self.full_name} salary after rise: {self.salary:,.2f} ^{self.raise_amount}%\n "

    def apply_tax(self):
        if self.salary <= 500000:
            return self.salary
        elif 500000 <= self.salary <= 1000000:
            taxable_amount = int(self.salary - 500000)
            self.salary = int(taxable_amount * 0.80)
            return self.salary + 500000
        else:
            taxable_amount = float(self.salary - 1000000)
            first_tax = taxable_amount * 0.7
            second_tax = float(0.8 * 500000)
            self.salary = first_tax + second_tax + 500000
            return self.salary

    def __repr__(self):
        return f'{self.__class__.__name__}("{self.first_name}", "{self.last_name}", {self.salary})'




