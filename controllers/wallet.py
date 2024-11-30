from models.account_wallet import Account
from services.wallet import WalletService


class WalletController:
    def __init__(self, logger):
        self.service = WalletService(logger)
        self.logger = logger

    def create(self, account: Account):
        self.logger.info("Call create function of WalletService")
        try:
            self.service.create(account)
        except Exception as e:
            self.logger.error(f"We have an Exception: {e}")
            raise
