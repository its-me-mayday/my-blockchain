import os


class Wallet:
    def __init__(self):
        self.amount = 0
        self.code = os.urandom(15).hex()

    def add(self, coins):
        self.amount += coins

    def remove(self, coins):
        self.amount -= (
            coins if self.check_balance() else print("Not sufficiently funds!")
        )

    def check_balance(self, coins):
        return (self.amount - coins) >= 0
