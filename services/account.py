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

    def deposit(self, account: Account, amount: float):
        self.logger.info(
            f"{account} is depositing {amount} coins in its wallet."
        )
        try:
            wallet = account.account_wallet.wallet
            self.logger.debug(f"{account} has wallet {wallet}")
            wallet.amount += amount
            self.logger.debug(
                f"{account} increases {wallet} "
                f"balance with {amount} coins."
            )
        except Exception as e:
            self.logger.error(f"We have an Exception: {e}")
            raise
