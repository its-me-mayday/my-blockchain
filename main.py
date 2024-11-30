from configs.logger import logger
from controllers.account import AccountController
from controllers.wallet import WalletController


def main():
    logger.info("A sends to B 1 MC (without gasfee)")

    account_controller = AccountController(logger)
    wallet_controller = WalletController(logger)

    accountA = account_controller.create_account("Alex")
    logger.info(f"Create Account {accountA}")
    accountB = account_controller.create_account("Bob")
    logger.info(f"Create Account {accountB}")

    wallet_controller.create_for(accountA)
    logger.info(f"Wallet {accountA.account_wallet.wallet.code} created!")
    wallet_controller.create_for(accountB)
    logger.info(f"Wallet {accountB.account_wallet.wallet.code} created!")

    account_controller.deposit(accountA, 10)


if __name__ == "__main__":
    main()
