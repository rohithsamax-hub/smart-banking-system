accounts = {}

def create_account(name, acc_no, pin):
    if acc_no in accounts:
        print("Account already exists!")
        return False
    accounts[acc_no] = {
        "name": name,
        "pin": pin,
        "balance": 0
    }
    return True