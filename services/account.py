from models.account_wallet import Account


class AccountService:
    def __init__(self, logger):
        self.logger = logger

    def create_account(self, username: str):
        try:
            account = Account(username)
        except Exception as e:
            self.logger.error(f"We have an Exception: {e}")
            raise

        self.logger.info(
            f"Account with username: {account.username} "
            f"is created succesfully! reference: {account}"
        )
        return account

    def deposit(self, account: Account, coin: float):
        self.logger.info(
            f"{account.username} is depositing {coin} MAYDAY coins"
        )
        try:
            wallet = account.account_wallet.wallet
            self.logger.info(f"{account.username} has wallet {wallet.code}")
            wallet.add(coin)
            self.logger.info(
                f"{account.username} increases wallet {wallet.code} "
                f"balance with {coin} MAYDAY coins."
            )
        except Exception as e:
            self.logger.error(f"We have an Exception: {e}")
            raise
