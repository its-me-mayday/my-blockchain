from models.account_wallet import Account


class Transaction:
    def __init__(self, sender: Account, receiver: Account, amount: float):
        self._sender = sender
        self._receiver = receiver
        self._amount = amount
        self._success = False

    @property
    def sender(self):
        return self._sender

    @property
    def receiver(self):
        return self._receiver

    @property
    def amount(self):
        return self._amount

    @property
    def success(self):
        return self._success

    @success.setter
    def success(self, new_success):
        self._success = new_success

    def __repr__(self):
        return f"Transaction(from: {self.sender}, "
        f"to: {self.receiver}, amount: {self.amount})"
