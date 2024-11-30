from models.account_model import Account


class AccountService:
    def __init__(self, account: Account, logger):
        self.account = account
        self.logger = logger

    def deposit(self, coin: float):
        wallet = self.account.wallet
        wallet.add(coin)
        self.logger.debug(
            f"Wallet {wallet.code} increases our balance to {wallet.amount} "
            f"MAYDAY coins. The deposit is {coin} MAYDAY coins"
        )
