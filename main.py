from configs.logger import logger
from controllers.account_controller import AccountController
from models.account_model import Account
from models.wallet_model import Wallet
from services.account_service import AccountService


def main():
    logger.info("A sends to B 1 MC (without gasfee)")
    walletA = Wallet()
    logger.info(f"Create Wallet {walletA}")
    logger.debug(
        f"WalletA has name: {walletA.code} "
        "and has {walletA.amount} MAYDAY coins"
    )
    walletB = Wallet()
    logger.info(f"Create Wallet {walletB}")
    logger.debug(
        f"WalletB has name: {walletB.code} "
        "and has {walletB.amount} MAYDAY coins"
    )

    accountA = Account("Alex", walletA)
    logger.info(f"Create Account {accountA}")
    logger.debug(
        f"AccountA has username: {accountA.username} "
        "and his wallet is the following: {accountA.wallet.code}"
    )
    accountB = Account("Bob", walletB)
    logger.info(f"Create Account {accountB}")
    logger.debug(
        f"AccountB has username: {accountB.username} "
        "and his wallet is the following: {accountB.wallet.code}"
    )

    serviceA = AccountService(accountA, logger)
    controllerA = AccountController(serviceA, logger)
    controllerA.deposit(10)
    logger.debug(
        f"WalletA has name: {walletA.code} "
        "and has {walletA.amount} MAYDAY coins"
    )


if __name__ == "__main__":
    main()
