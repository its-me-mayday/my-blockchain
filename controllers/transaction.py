from services.transaction import TransactionService
from models.account_wallet import Account


class TransactionController:
    def __init__(self, logger):
        self.service = TransactionService(logger)
        self.logger = logger

    def create(self, sender: Account, receiver: Account, amount: float):
        self.logger.info("Call create function of TransactionService")
        try:
            transaction = self.service.create(sender, receiver, amount)
            transaction.success = True
        except Exception as e:
            self.logger.error(f"We have an Exception: {e}")
            raise

        self.logger.debug(f"Return {transaction}")
        return transaction
