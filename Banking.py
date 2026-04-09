import sys

class BankAccount:
    def __init__(self, name, acc_no, pin, balance=0):
        self.name = name
        self.acc_no = acc_no
        self.pin = pin
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        if amount > 0:

            self.balance += amount
            self.transactions.append(f"Deposited: {amount}")
            print("Amount Deposited Successfully!")
        else:
            print("Invalid Amount!")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Balance!")
        elif amount <= 0:
            print("Invalid Amount!")
        else:
            self.balance -= amount
            self.transactions.append(f"Withdrawn: {amount}")
            print("Amount Withdrawn Successfully!")

    def check_balance(self):
        print("Available Balance:", self.balance)

    def account_details(self):
        print("\n--- Account Details ---")
        print("Name:", self.name)
        print("Account Number:", self.acc_no)
        print("Balance:", self.balance)

    def show_transactions(self):
        print("\n--- Transaction History ---")
        if not self.transactions:
            print("No transactions yet.")
        else:
            for t in self.transactions:
                print(t)


accounts = {}


def create_account():
    print("\n--- Create Account ---")
    name = input("Enter Name: ")
    acc_no = input("Enter Account Number: ")
    pin = input("Set 4-digit PIN: ")

    if acc_no in accounts:
        print("Account already exists!")
    else:
        accounts[acc_no] = BankAccount(name, acc_no, pin)
        print("Account Created Successfully!")


def login():
    print("\n--- Login ---")
    acc_no = input("Enter Account Number: ")
    pin = input("Enter PIN: ")

    if acc_no in accounts and accounts[acc_no].pin == pin:
        print("Login Successful!")
        account_menu(accounts[acc_no])
    else:
        print("Invalid Account Number or PIN!")


def account_menu(account):
    while True:
        print("\n--- Account Menu ---")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Account Details")
        print("5. Transaction History")
        print("6. Logout")

        option = input("Enter option (1-6): ")

        if option == "1":
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)

        elif option == "2":
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)

        elif option == "3":
            account.check_balance()

        elif option == "4":
            account.account_details()

        elif option == "5":
            account.show_transactions()

        elif option == "6":
            print("Logged out successfully!")
            break

        else:
            print("Invalid option! Please enter between 1 and 6.")


while True:
    print("\n========================================")
    print(" SMART BANKING SYSTEM ")
    print("========================================")
    print("1. Create Account")
    print("2. Login")
    print("3. Exit")
    print("========================================")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        create_account()

    elif choice == "2":
        login()

    elif choice == "3":
        print("Thank you for using Smart Banking System!")
        sys.exit()

    else:
        print("Invalid choice! Please enter 1, 2, or 3.")