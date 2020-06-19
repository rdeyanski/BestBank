class User:
    def __init__(self, first_name, last_name, phone, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email
        self.password = password

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_phone(self):
        return self.phone

    def get_email(self):
        return self.email

    def get_password(self):
        return self.password

    def __str__(self):
        return f'\n{self.get_first_name()} {self.get_last_name()} {self.get_phone()} {self.get_email()} {self.get_password()}'


class Customer(User):
    def __init__(self, first_name, last_name, phone, email, password, customer_id):
        self.customer_id = customer_id
        super().__init__(first_name, last_name, phone, email, password)

    def get_customer_id(self):
        return self.customer_id


class Company(Customer):
    def __init__(self, first_name, last_name, phone, email, password, customer_id, company_name):
        self.company_name = company_name
        super().__init__(first_name, last_name, phone, email, password, customer_id)

    def get_company_name(self):
        return self.company_name


class Person(Customer):
    def __init__(self, first_name, last_name, phone, email, password, customer_id, address):
        self.address = address
        super().__init__(first_name, last_name, phone, email, password, customer_id)


class Staff(User):
    def __init__(self, first_name, last_name, phone, email, password, title):
        self.title = title
        super().__init__(first_name, last_name, phone, email, password)


class Admin(Staff):
    def __init__(self, first_name, last_name, phone, email, password, title, admin_id):
        self.admin_id = admin_id
        super().__init__(first_name, last_name, phone, email, password, title)


class Employee(Staff):
    def __init__(self, first_name, last_name, phone, email, password, title, empl_id):
        self.empl_id = empl_id
        super().__init__(first_name, last_name, phone, email, password, title)




