from models.wallet_model import Wallet


class Account:
    def __init__(self, username: str, wallet: Wallet):
        self.username = username
        self.wallet = wallet

    def deposit(self, coin):
        self.wallet.amount += coin
