from configs.logger import logger
from controllers.factories import (
    create_account_controller,
    create_wallet_controller,
    create_transaction_controller,
)


def main():
    logger.info("Simulation: A sends to B 10 MC (without gasfee)")

    account_controller = create_account_controller(logger)
    wallet_controller = create_wallet_controller(logger)
    transaction_controller = create_transaction_controller(logger)

    accountA = account_controller.create_account("Alex")
    logger.info(f"Create Account {accountA}")
    accountB = account_controller.create_account("Bob")
    logger.info(f"Create Account {accountB}")

    wallet_controller.create_wallet(accountA)
    logger.info(f"Wallet {accountA.account_wallet.wallet.code} created!")
    wallet_controller.create_wallet(accountB)
    logger.info(f"Wallet {accountB.account_wallet.wallet.code} created!")

    account_controller.deposit(accountA, 10)

    transaction_controller.create(accountA, accountB, 10.0)


if __name__ == "__main__":
    main()
