import pandas as pd

def show_accounts_table(accounts):
    if not accounts:
        print("No data")
        return
    df = pd.DataFrame(accounts).T
    print("\nAccount Data:\n", df)