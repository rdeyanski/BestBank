class Transaction:
    def __init__(self, account_id, amount: float, date_time):
        self.account_id = account_id
        self.amount = amount
        self.date_time = date_time

        def get_account_id(self):
            return self.account_id

        def get_amount(self):
            return self.amount

        def get_date_time(self):
            return self.date_time


class Deposit(Transaction):
    pass


class Withdraw(Transaction):
    pass
