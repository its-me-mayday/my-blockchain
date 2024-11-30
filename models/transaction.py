from models.account_wallet import Account
import time


class Transaction:
    def __init__(self, sender: Account, receiver: Account, amount: float):
        self._sender = sender
        self._receiver = receiver
        self._amount = amount
        self._created_at = time.asctime()
        self._updated_at = time.asctime()

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
    def created_at(self):
        return self._created_at

    @property
    def updated_at(self):
        return self._updated_at

    @updated_at.setter
    def updated_at(self, new_update_at):
        self._update_at = new_update_at

    def __repr__(self):
        return (
            f"Transaction(from: {self.sender}, "
            f"to: {self.receiver}, amount: {self.amount}, "
            f"created_at: {self._created_at}, "
            f"updated_at: {self._updated_at})"
        )
