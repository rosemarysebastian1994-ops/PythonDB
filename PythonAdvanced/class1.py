# Define a class named Account with attributes account_number, account_name, balance and methods
# withdraw(), deposit(), show_balance(). Create the account object and call each method.
class Account:
    def __init__(self):
        self.acc_no = int(input("Enter the account number: "))
        self.acc_name = input("Enter the account name: ")
        self.balance = int(input("Enter the balance: "))
    def withdraw(self):
        amount = int(input("Enter the amount to withdraw: "))
        self.balance -= amount
    def deposit(self):
        amount = int(input("Enter the amount to deposit: "))
        self.balance += amount
    def show_balance(self):
        print("The current balance is: ", self.balance)
a = Account()
a.withdraw()
a.deposit()
a.show_balance()