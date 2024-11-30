from models.account_model import Account


class AccountService:
    def __init__(self, account: Account, logger):
        self.account = account
        self.logger = logger

    def deposit(self, coin: float):
        self.logger.info(
            f"{self.account.username} is depositing {coin} MAYDAY coins"
        )
        try:
            wallet = self.account.wallet
            self.logger.info(
                f"{self.account.username} has wallet {wallet.code}"
            )
            wallet.add(coin)
            self.logger.info(
                f"{self.account.username} increases wallet {wallet.code} "
                f"balance with {coin} MAYDAY coins."
            )
        except Exception as e:
            self.logger.error(f"We have an Exception: {e}")
            raise
