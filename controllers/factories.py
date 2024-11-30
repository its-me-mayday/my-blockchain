from controllers.account import AccountController
from controllers.wallet import WalletController
from controllers.transaction import TransactionController


def create_account_controller(logger):
    return AccountController(logger)


def create_transaction_controller(logger):
    return TransactionController(logger)


def create_wallet_controller(logger):
    return WalletController(logger)
