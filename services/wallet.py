from models.account_wallet import Account, AccountWallet, Wallet


class WalletService:
    def __init__(self, logger):
        self.logger = logger

    def create_for(self, account: Account):
        wallet = Wallet(account)
        self.logger.info(
            f"Wallet with code: {wallet.code} "
            f"is created succesfully by {wallet.account.username}!"
        )
        account_wallet_created = AccountWallet(account, wallet)
        self.logger.debug(
            "AccountWallet is created: "
            f"{account_wallet_created.account.username} as account (username) "
            f"and {account_wallet_created.wallet.code} as wallet (code)"
        )

        self.logger.debug(f"account_wallet: {account.account_wallet}")
        account.account_wallet = account_wallet_created
        self.logger.debug(f"account_wallet: {account.account_wallet}")
        self.logger.info(
            "Account is associated to Wallet: "
            f"account {account.username} "
            f"wallet {account.account_wallet.wallet.code} as wallet (code)"
        )
