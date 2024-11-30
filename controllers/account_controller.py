from services.account_service import AccountService


class AccountController:
    def __init__(self, service: AccountService, logger):
        self.service = service
        self.logger = logger

    def deposit(self, coin: float):
        self.service.exec_deposit(coin)
