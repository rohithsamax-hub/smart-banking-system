from week6_oop import BankAccount

class PremiumAccount(BankAccount):
    def deposit(self, amount):
        bonus = 10
        self.balance += amount + bonus