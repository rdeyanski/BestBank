class Update:
    def __init__(self, old_detail, new_detail, date_time):
        self.old_detail = old_detail
        self.new_detail = new_detail
        self.date_time = date_time

        def get_old_detail(self):
            return self.old_detail

        def get_new_detail(self):
            return self.new_detail

        def get_date_time(self):
            return self.date_time


class AccountUpdate(Update):
    def __init__(self, acc_id, old_detail, new_detail, date_time):
        self.acc_id = acc_id
        super().__init__(old_detail, new_detail, date_time)


class TransferUpdate(Update):
    def __init__(self, acc_id, old_detail, new_detail, date_time):
        self.acc_id = acc_id
        super().__init__(old_detail, new_detail, date_time)


class UserUpdate(Update):
    def __init__(self, user_name, old_detail, new_detail, date_time):
        self.user_name = user_name
        super().__init__(old_detail, new_detail, date_time)
