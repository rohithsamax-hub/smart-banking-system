import numpy as np

def total_bank_balance(accounts):
    balances = np.array([acc["balance"] for acc in accounts.values()])
    return np.sum(balances)