def deposit(balance, amount):
    if amount > 0:
        return balance + amount
    return balance

def withdraw(balance, amount):
    if amount > balance:
        print("Insufficient balance!")
        return balance
    elif amount <= 0:
        print("Invalid amount!")
        return balance
    return balance - amount