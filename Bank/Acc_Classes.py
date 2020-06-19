class Account:
    def __init__(self, account_id, balance: float, interest: float, owner):
        self.account_id = account_id
        self.owner = owner
        self.balance = balance
        self.interest = interest

    def get_account_id(self):
        return self.account_id

    def get_balance(self):
        return self.balance

    def get_interest(self):
        return self.interest

    def get_owner(self):
        return self.owner

    def __del__(self):
        return 'deleted'


class DepositAccount(Account):
    def __init__(self, account_id, balance: float, interest, owner):
        super().__init__(account_id, balance, interest, owner)


class CreditAccount(Account):
    def __init__(self, account_id, balance: float, interest, owner, pay_per_month: float):
        self.pay_per_month = pay_per_month
        super().__init__(account_id, balance, interest, owner)

    def get_pay_per_month(self):
        return self.pay_per_month


class MortgageAccount(CreditAccount):
    def __init__(self, account_id, balance, interest, owner, pay_per_month):
        super().__init__(account_id, balance, interest, owner, pay_per_month )
