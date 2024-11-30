from models.wallet_model import Wallet


class Account:
    def __init__(self, username: str, wallet: Wallet):
        self._username = username
        self._wallet = wallet

    @property
    def username(self):
        return self._username

    @property
    def wallet(self):
        return self._wallet

    @wallet.setter
    def wallet(self, new_wallet: Wallet):
        self.wallet = new_wallet
