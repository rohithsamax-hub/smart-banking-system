def get_amount():
    try:
        return float(input("Enter amount: "))
    except:
        print("Invalid input!")
        return 0