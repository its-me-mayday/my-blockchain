import os


class Account:
    def __init__(self, username: str, account_wallet=None):
        self._username = username
        self._account_wallet = (
            account_wallet
            if account_wallet is not None
            else AccountWallet(self)
        )

    @property
    def username(self):
        return self._username

    @property
    def account_wallet(self):
        return self._account_wallet

    @account_wallet.setter
    def account_wallet(self, new_account_wallet):
        self._account_wallet = new_account_wallet

    def __repr__(self):
        return f"Account(username: {self.username})"


class Wallet:
    def __init__(self, account: Account):
        self._amount = 0
        self._code = os.urandom(15).hex()
        self._account = account

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, new_amount):
        self._amount = new_amount

    @property
    def code(self):
        return self._code

    @property
    def account(self):
        return self._account

    def __repr__(self):
        return f"Wallet(code: {self.code}, amount: {self.amount})"


class AccountWallet:
    def __init__(self, account: Account, wallet: Wallet = None):
        self._account = account
        self._wallet = wallet

    @property
    def account(self):
        return self._account

    @property
    def wallet(self):
        return self._wallet

    @wallet.setter
    def wallet(self, new_wallet: Wallet):
        self._wallet = new_wallet

    def __repr__(self):
        return f"AccountWallet(account: {self.account}, wallet: {self.wallet})"
