from models.account_wallet import Account
from services.account import AccountService


class AccountController:
    def __init__(self, logger):
        self.service = AccountService(logger)
        self.logger = logger

    def create_account(self, username: str):
        self.logger.info("Call create function of AccountService")
        try:
            account = self.service.create_account(username)
        except Exception as e:
            self.logger.error(f"We have an Exception: {e}")
            raise

        self.logger.debug(f"Return Account: {account}")
        return account

    def deposit(self, account: Account, coin: float):
        self.logger.info("Call deposit function of AccountService")
        try:
            self.service.deposit(account, coin)
        except Exception as e:
            self.logger.error(f"We have an Exception: {e}")
            raise
