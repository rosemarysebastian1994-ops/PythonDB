class Account:
    def __init__(self):
        self.acct_no = int(input("Enter the account number: "))
        self.acct_name = input("Enter the account name: ")
        self.balance = int(input("Enter the balance: "))
    def withdraw(self):
        self.amount = int(input("Enter the amount to withdraw: "))
        self.balance -= self.amount

    def deposit(self):
        self.amount = int(input("enter the amount:"))
        self.balance += self.amount

    def show_balance(self):
        print("the current balance is:", self.balance)

l = []

while 1:
    print("1. Create account")
    print("2. Withdraw")
    print("3. Deposit")
    print("4. Show balance")
    print("5. Exit")
    ch = int(input("Enter the choice: "))
    if ch == 1:
        a = Account()
        l.append(a)
        for i in l:
            print(i.acct_no, i.acct_name, i.balance)
    elif ch == 2:
        n = int(input("Enter the account number: "))
        for i in l:
            if i.acct_no == n:
                i.withdraw()
                break
        else:
            print("Account not found")
    elif ch == 3:
        n = int(input("Enter the account number: "))
        for i in l:
            if i.acct_no == n:
                i.deposit()
                break
        else:
            print("Account not found")
    elif ch == 4:
        n = int(input("Enter the account number: "))
        for i in l:
            if i.acct_no == n:
                i.show_balance()
                break
        else:
            print("Account not found")
    elif ch == 5:
        exit()
    else:
        pass