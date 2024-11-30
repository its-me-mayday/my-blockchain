from services.account_service import AccountService


class AccountController:
    def __init__(self, service: AccountService, logger):
        self.service = service
        self.logger = logger

    def deposit(self, coin: float):
        self.logger.info("Call deposit function of AccountService")
        try:
            self.service.deposit(coin)
        except Exception as e:
            self.logger.error(f"We have an Exception: {e}")
            raise
