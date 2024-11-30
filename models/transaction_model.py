from models.account_wallet import Account


class Transaction:
    def __init__(self, source: Account, dest: Account, amount: float):
        self.source = source
        self.dest = dest
        self.amount = amount
