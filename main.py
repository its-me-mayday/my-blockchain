from configs.logger import logger
from controllers.account_controller import AccountController
from models.account_model import Account
from models.wallet_model import Wallet
from services.account_service import AccountService


def main():
    logger.info("A sends to B 1 MC (without gasfee)")
    walletA = Wallet()
    logger.info(f"Wallet {walletA.code} created!")
    walletB = Wallet()
    logger.info(f"Wallet {walletB.code} created!")

    accountA = Account("Alex", walletA)
    logger.info(f"Create Account {accountA}")

    accountB = Account("Bob", walletB)
    logger.info(f"Create Account {accountB}")

    serviceA = AccountService(accountA, logger)
    controllerA = AccountController(serviceA, logger)
    controllerA.deposit(10)


if __name__ == "__main__":
    main()
