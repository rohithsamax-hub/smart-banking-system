import json

def save_data(accounts):
    with open("data.json", "w") as f:
        json.dump(accounts, f)

def load_data():
    try:
        with open("data.json", "r") as f:
            return json.load(f)
    except:
        return {}