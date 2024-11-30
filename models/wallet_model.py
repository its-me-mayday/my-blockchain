import os


class Wallet:
    def __init__(self):
        self._amount = 0
        self._code = os.urandom(15).hex()

    @property
    def amount(self):
        return self._amount

    @property
    def code(self):
        return self._code

    def add(self, coins):
        self._amount += coins

    def remove(self, coins):
        self._amount -= (
            coins
            if self._check_balance()
            else print("Not sufficiently funds!")
        )

    def _check_balance(self, coins):
        return (self._amount - coins) >= 0
