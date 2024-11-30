from controllers.account import AccountController
from controllers.wallet import WalletController


def create_account_controller(logger):
    return AccountController(logger)


def create_wallet_controller(logger):
    return WalletController(logger)
