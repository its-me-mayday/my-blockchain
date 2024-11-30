from models.account_wallet import Account
from services.account import AccountService
from services.wallet import WalletService
from services.transaction import TransactionService


class AccountController:
    def __init__(self, logger):
        self.service = AccountService(logger)
        self.wallet_service = WalletService(logger)
        self.transaction_service = TransactionService(logger)
        self.logger = logger

    def create(self, username: str):
        self.logger.info("Call create function of AccountService")
        try:
            account = self.service.create(username)
        except Exception as e:
            self.logger.error(f"We have an Exception: {e}")
            raise

        self.logger.debug(f"Return Account: {account}")
        return account

    def deposit(self, account: Account, amount: float):
        self.logger.info("Call deposit function of WalletService")
        try:
            deposit_result = self.wallet_service.deposit(account, amount)
            self.logger.debug(f"Deposit result: {deposit_result}")
        except Exception as e:
            self.logger.error(f"We have an Exception: {e}")
            raise
        return deposit_result

    def transfer(self, sender: Account, receiver: Account, amount: float):
        self.logger.info(
            "Call transfer fn of WalletService "
            "and create fn of TransactionService"
        )
        self.logger.debug(
            f"Sender account: {sender}, Receiver account: {receiver}"
        )
        try:
            transfer_result = self.wallet_service.transfer(
                sender, receiver, amount
            )
            self.logger.debug(f"Transfer result: {transfer_result}")
            if not transfer_result:
                self.logger.error(
                    "Transfer is failed because it's not affordable!"
                )
                return False
            self.logger.info("Tranfer is OK. Creating transaction..")
            transaction_result = self.transaction_service.create(
                sender, receiver, amount
            )
            self.logger.info(
                f"Transaction {transaction_result} created successfully!"
            )
        except Exception as e:
            self.logger.error(f"We have an Exception: {e}")
            raise
