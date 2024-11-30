from configs.logger import logger
from controllers.account import AccountController
from controllers.wallet import WalletController
from models.account_wallet import Account
from services.account import AccountService


def main():
    logger.info("A sends to B 1 MC (without gasfee)")

    accountA = Account("Alex")
    logger.info(f"Create Account {accountA}")
    accountB = Account("Bob")
    logger.info(f"Create Account {accountB}")

    wallet_controller = WalletController(logger)
    wallet_controller.create_for(accountA)
    logger.info(f"Wallet {accountA.account_wallet.wallet.code} created!")
    wallet_controller.create_for(accountB)
    logger.info(f"Wallet {accountB.account_wallet.wallet.code} created!")

    serviceA = AccountService(accountA, logger)
    controllerA = AccountController(serviceA, logger)
    controllerA.deposit(10)


if __name__ == "__main__":
    main()
