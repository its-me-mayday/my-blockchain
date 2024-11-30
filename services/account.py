from models.account_wallet import Account


class AccountService:
    def __init__(self, logger):
        self.logger = logger

    def create(self, username: str):
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
