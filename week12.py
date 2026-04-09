import matplotlib.pyplot as plt

def plot_balances(accounts):
    if not accounts:
        print("No data to plot")
        return

    names = list(accounts.keys())
    balances = [accounts[a]["balance"] for a in names]

    plt.bar(names, balances)
    plt.xlabel("Account Number")
    plt.ylabel("Balance")
    plt.title("Bank Balance Chart")
    plt.show()