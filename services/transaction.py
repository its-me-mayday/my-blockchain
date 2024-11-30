from models.account_wallet import Account
from models.transaction import Transaction


class TransactionService:
    def __init__(self, logger):
        self.logger = logger

    def create(self, sender: Account, receiver: Account, amount: float):
        transaction = Transaction(sender, receiver, amount)
        self.logger.info(f"Transaction created: {transaction}")

        return transaction
