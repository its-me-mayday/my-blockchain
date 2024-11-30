from models.account_wallet import Account, AccountWallet, Wallet


class WalletService:
    def __init__(self, logger):
        self.logger = logger

    def create_wallet(self, account: Account):
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

    def transfer(self, sender: Account, receiver: Account, amount: float):
        self.logger.info(
            f"Sender: {sender} has to send {amount} coins to"
            f"receiver: {receiver}"
        )
        sender_wallet = sender.account_wallet.wallet
        self.logger.info(f"Sender wallet: {sender_wallet}")
        receiver_wallet = receiver.account_wallet.wallet
        self.logger.info(f"Receiver wallet: {receiver_wallet}")

        affordable = self._is_affordable(sender_wallet, amount)
        self.logger.debug(f"is_affordable?: {affordable}")
        if not affordable:
            return False

        self.logger.debug(
            f"sender_wallet amount (before payment): {sender_wallet}"
        )
        self.logger.debug(
            f"receiver_wallet amount (before payment): {receiver_wallet}"
        )
        sender_wallet.amount -= amount
        self.logger.debug(
            f"sender_wallet amount (after payment): {sender_wallet}"
        )
        receiver_wallet.amount += amount
        self.logger.debug(
            f"receiver_wallet amount (after payment): {receiver_wallet}"
        )

        return True

    def _is_affordable(self, wallet, amount):
        return True if wallet.amount - amount >= 0 else False
