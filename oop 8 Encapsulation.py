# Encapsulation:
# Encapsulation is the process of hiding implementation details from the outside world.
# In Python, encapsulation is typically achieved by making class attributes and methods private,
# using the double underscore (__) prefix.

class BankAccount:
    def __init__(self, Account_number, Balance):
        self.__Account_number = Account_number
        self.__Balance = Balance

    def get_full_details(self):
        return f"Account Number: {self.__Account_number}\nBalance: {self.__Balance}\n"

    def add_amount(self, amount):
        self.__Balance += amount
        return f"Added Amount: ${amount:,}\nCurrent Balance: ${self.__Balance:,.2f}\n"

    def withdraw_amount(self, amount):
        if self.__Balance > amount:
            self.__Balance -= amount
            return f"Amount Withdraw: ${amount:,}\nCurrent Amount: ${self.__Balance:,.2f}\n"
        else:
            return f"Oops!!, Insufficient Balance"

    def check_balance(self):
        return f"Current Account Balance: ${self.__Balance:,.2f}\n"

    def __bank_details(self):
        return f"{self.__Account_number}"


cust1 = BankAccount(9390030998, 5000000)
print(cust1.check_balance())
print(cust1.add_amount(50000))
print(cust1.withdraw_amount(500000))
# You can access private method using:
print(cust1._BankAccount__bank_details())