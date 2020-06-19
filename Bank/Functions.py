import pickle
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

from Bank.Acc_Classes import DepositAccount, CreditAccount, MortgageAccount
from Bank.Transactions import Deposit, Withdraw
from Bank.Updates import UserUpdate, AccountUpdate, TransferUpdate
from Bank.User_Classes import Company, Person, Admin, Employee, Staff

with open('users_inventory', 'rb') as users_inventory_file:
    users_inventory = pickle.load(users_inventory_file)

with open('accounts_inventory', 'rb') as accounts_inventory_file:
    accounts_inventory = pickle.load(accounts_inventory_file)

with open('transactions_inventory', 'rb') as transactions_inventory_file:
    transactions_inventory = pickle.load(transactions_inventory_file)

with open('updates_inventory', 'rb') as updates_inventory_file:
    updates_inventory = pickle.load(updates_inventory_file)


def current_time():
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print(dt_string, '\n')


def welcome():
    """ Greets the user and gives options to enter the system """
    print('\n', '=' * 41, '\n|',
          '   Welcome in BestBank Online System!    '
          '|\n|', '*' * 40, '|\n|', ' ' * 40, '|',
          '\n| 1. Login.', ' ' * 30, '|',
          '\n| 2. Register (new user).', ' ' * 16, '|',
          '\n| 3. Interest Calculator.', ' ' * 16, '|'
          '\n| 4. Quit.', ' ' * 31, '|',
          '\n|', ' ' * 40, '|',
          '\n| Please, enter one of the options above:  |',
          '\n|', '-' * 40, '|')


def register():
    """ Registers new user in the system """
    # users_inventory = []
    # updates_inventory = []
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y at %H:%M:%S")

    first_name = input('\nEnter first name:\t')
    last_name = input('Enter last name:\t')
    phone = input('Enter your phone number:\t')
    email = input('Enter your email address:\t')
    new_password = input('Enter your password:\t')
    re_password = input('Repeat your password:\t')
    while new_password != re_password:
        print('Repeat incorrect! Please enter and re-enter your password:\t')
        command1 = input()
        command2 = input()
        if command1 == command2:
            new_password = re_password = command2
    password = new_password

    mark1 = email
    mark2 = password[-5::]
    if mark1.split('@')[1] == 'bestbank.eu':
        title = input('\nEnter your title:\t')
        admin_id = input('\nEnter your ID:\t')
        if mark2 == 'admin':
            users_inventory.append(Admin(first_name, last_name, phone, email, password, title, admin_id))
        elif mark2 == 'staff':
            empl_id = admin_id
            users_inventory.append(Employee(first_name, last_name, phone, email, password, title, empl_id))
        else:
            print('\n', '=' * 38,
                  '\nInvalid Registration!'
                  '\nPlease, try again, or contact us in person.'
                  f'\nThank you!\n{dt_string}', '-' * 38)
            pass
        user_name = first_name + last_name
        old_detail = 'Staff'
        new_detail = password
        date_time = dt_string
        updates_inventory.append(UserUpdate(user_name, old_detail, new_detail, date_time))
        print(f'\nCongratulations, {first_name} {last_name}!,\n'
              f'You successfully joined Best Bank Team as {title}.')
        with open('users_inventory', 'wb') as users_inventory_file:
            pickle.dump(users_inventory, users_inventory_file)
        with open('updates_inventory', 'wb') as updates_inventory_file:
            pickle.dump(updates_inventory, updates_inventory_file)

    else:
        command = input('\nWhat type of online banking you register?'
                        '\n1. Business.'
                        '\n2. Personal.'
                        '\nPlease, enter one of the options above:\t')
        type = None
        if command == '1':
            customer_id = input('Enter your company ID:\t')
            company_name = input('Enter company name:\t')
            users_inventory.append(Company(first_name, last_name, phone, email, password, customer_id, company_name))
            type = 'Business'
        if command == '2':
            customer_id = input('Enter your personal ID:\t')
            address = input('Enter postal address:\t')
            users_inventory.append(Person(first_name, last_name, phone, email, password, customer_id, address))
            type = 'Personal'
        user_name = first_name + last_name
        old_detail = type
        new_detail = password
        date_time = dt_string
        updates_inventory.append(UserUpdate(user_name, old_detail, new_detail, date_time))
        print(f'\n Congrats {first_name} {last_name}!'
              f'\n You are registered as {type} Customer'
              f'\n on {dt_string}'
              f'\n IMPORTANT:'
              f'\n Please, wait SMS confirming your bank account,'
              f'\n then login and change your password first. Thank you!')
        with open('users_inventory', 'wb') as users_inventory_file:
            pickle.dump(users_inventory, users_inventory_file)
        with open('updates_inventory', 'wb') as updates_inventory_file:
            pickle.dump(updates_inventory, updates_inventory_file)


def all_users_list():
    """ Displays all users in the system """
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y at %H:%M:%S")

    def print_user_list():
        mark = None
        if type(user) is Person:
            mark = 'Personal:'
        if type(user) is Company:
            mark = 'Business:'
        if type(user) is Admin or type(user) is Employee:
            mark = user.title + ':'
        print('{:.<28}'.format(mark + ' ' + user.first_name + ' ' + user.last_name),
              '{:.<17}'.format(user.phone), '{:.<21}'.format(user.email), '{:>10}'.format(user.password))

    command = input('\n 1. New Applicants.'
                    '\n 2. Current Users.'
                    '\n 3. Staff.'
                    '\n 4. <= Back'
                    '\n   Enter one of the options above:\t')

    if command == '1':
        print('\n\n|', '=' * 25, ' NEW APPLICANTS REPORT ', '=' * 25, '|',
              '\n| type/first/last name ----- phone number ----'
              ' email address ------- password |\n|', ' ' * 75, '|')
        for user in users_inventory:
            flag = True
            for account in accounts_inventory:
                if user.password == account.owner:
                    flag = True
                    break
                else:
                    flag = False
            if not flag:
                print_user_list()

    if command == '2':
        print('\n\n|', '=' * 27, ' USERS LIST REPORT ', '=' * 27,
              '|\n| type/first/last name ----- phone number ----'
              ' email address ------- password |\n|', ' ' * 75, '|')
        for user in users_inventory:
            for account in accounts_inventory:
                if user.password != account.owner:
                    continue
                else:
                    print_user_list()
                    break

    if command == '3':
        print('\n\n|', '=' * 26, ' STAFF LIST REPORT ', '=' * 28,
              '|\n| title/first/last name ----- phone number ----'
              ' email address ------ password |\n|', ' ' * 75, '|')
        for user in users_inventory:
            if type(user) is Admin or type(user) is Employee:
                print_user_list()
    print('|', ' ' * 75, '|\n|', '-' * 36,
          f'Report done on: {dt_string} |')


def user_update():
    """ Updates User's Profile """
    # updates_inventory = []
    now = datetime.now()
    dt_string = now.strftime(" %d/%m/%Y %H:%M:%S ")

    def print_users_details():
        print('1. First name: ', '{:.>22}'.format(user.first_name),
              '\n2. Last name: ', '{:.>23}'.format(user.last_name),
              '\n3. Phone number: ', '{:.>20}'.format(user.phone),
              '\n4. Email address: ', '{:.>19}'.format(user.email),
              '\n5. Password: ', '{:.>24}'.format(user.password))
        if type(user) is Person:
            print('6. Mail address: ', '{:.>20}'.format(user.address))
        if type(user) is Company:
            print('6. Company name: ', '{:.>20}'.format(user.company_name))
        if type(user) is Admin or type(user) is Employee:
            print('6. Job title: ', '{:.>18}'.format(user.title))

    password = input('\n Enter password:\t')
    flag = None
    for user in users_inventory:
        if user.password != password:
            pass
        if user.password == password:
            flag = True
            user_name = user.first_name + ' ' + user.last_name
            old_detail = None
            new_detail = None
            print()
            print('=' * 38)
            print('---------- Current Profile ----------')
            print_users_details()
            command = input(f'\nPlease, enter from 1 to 6, which detail'
                            f'\nyou would like to update:\t')
            if command == '1':
                old_detail = user.first_name
                new_detail = input('\nEnter first name:\t')
                user.first_name = new_detail
            if command == '2':
                old_detail = user.last_name
                new_detail = input('\nEnter last name:\t')
                user.last_name = new_detail
            if command == '3':
                old_detail = user.phone
                new_detail = input('\nEnter new phone number:\t')
                user.phone = new_detail
            if command == '4':
                old_detail = user.email
                new_detail = input('\nEnter new email address:\t')
                user.email = new_detail
            if command == '5':
                old_detail = user.password
                old_password = password
                new_password = input('\nEnter new password:\t')
                re_password = input('\nRepeat new password:\t')
                while new_password != re_password:
                    print('\nRepeat incorrect! Please enter and re-enter new password:\t')
                    command1 = input()
                    command2 = input()
                    if command1 == command2:
                        new_password = re_password = command2
                new_detail = new_password
                user.password = new_detail
                for account in accounts_inventory:
                    if account.owner == old_password:
                        account.owner = user.password
            if command == '6':
                if type(user) is Person:
                    old_detail = user.address
                    new_detail = input('\nEnter new mail address:\t')
                    user.address = new_detail
                if type(user) is Company:
                    old_detail = user.company_name
                    new_detail = input('\nEnter new company name:\t')
                    user.company_name = new_detail
                if type(user) is Admin or type(user) is Employee:
                    old_detail = user.company_name
                    new_detail = input('\nEnter new title:\t')
                    user.company_name = new_detail
            updates_inventory.append(UserUpdate(user_name, old_detail, new_detail, dt_string))
            print('\nYour detail was successfully updated!\n\n',
                  '=' * 37, '\n------------ New Profile ------------')
            print_users_details()
            print('-' * 38, f'\n   Time of Record:{dt_string}\n', '=' * 38)
            with open('users_inventory', 'wb') as users_inventory_file:
                pickle.dump(users_inventory, users_inventory_file)
            with open('accounts_inventory', 'wb') as accounts_inventory_file:
                pickle.dump(accounts_inventory, accounts_inventory_file)
            with open('updates_inventory', 'wb') as updates_inventory_file:
                pickle.dump(updates_inventory, updates_inventory_file)
    if not flag:
        print('\n Invalid Password!')


def new_account():
    """ Opens new bank account """
    # accounts_inventory = []
    # updates_inventory = []
    now = datetime.now()
    dt_string = now.strftime(" %d/%m/%Y at %H:%M:%S ")

    def print_new_account():
        print('\n NEW ACCOUNT REGISTERED:'
              '\n -----------------------',
              f'\n Account Owner:       {user.first_name} {user.last_name}'
              f'\n Account N:           {account.account_id}'
              f'\n Account Balance: ', '{:{width}.{prec}f}'.format(account.balance, width=10, prec=2), 'lv.'
                                                                                                       f'\n Account Interest:     {account.interest} %.')
        if account_id[0] == '2':
            print(f' Pay per month: ', '{:{width}.{prec}f}'.format(account.pay_per_month, width=12, prec=2), 'lv.')
        print(f' Recorded on:{dt_string}', '\n', '-' * 36)

    owner = input("\n\n Enter the account owner's password:\t")
    account_id = input(' Enter 6 digit bank account number:\t')
    balance = float(input(' Enter account balance:\t'))
    interest = float(input(' Enter the account interest:\t'))

    if account_id[0] == '1' and len(account_id) == 6:
        accounts_inventory.append(DepositAccount(account_id, balance, interest, owner))
        for account in accounts_inventory:
            if account.account_id == account_id:
                for user in users_inventory:
                    if account.owner == user.password:
                        print_new_account()
    if account_id[0] == '2' and len(account_id) == 6:
        pay_per_month = float(input(' Enter the amount pay per month:\t'))
        if account_id[1] == '1':
            accounts_inventory.append(CreditAccount(account_id, balance, interest, owner, pay_per_month))
        if account_id[1] == '2':
            accounts_inventory.append(MortgageAccount(account_id, balance, interest, owner, pay_per_month))
        for account in accounts_inventory:
            if account.account_id == account_id:
                for user in users_inventory:
                    if account.owner == user.password:
                        print_new_account()
    acc_id = account_id
    old_detail = 'new_acc'
    new_detail = owner
    updates_inventory.append(AccountUpdate(acc_id, old_detail, new_detail, dt_string))
    with open('updates_inventory', 'wb') as updates_inventory_file:
        pickle.dump(updates_inventory, updates_inventory_file)
    with open('accounts_inventory', 'wb') as accounts_inventory_file:
        pickle.dump(accounts_inventory, accounts_inventory_file)


def new_user_account():
    """ Opens first bank account for new user """

    def print_user_list():
        mark = None
        if type(user) is Person:
            mark = 'Personal:'
        if type(user) is Company:
            mark = 'Business:'
        if type(user) is Admin or type(user) is Employee:
            mark = user.title + ':'
        print('{:.<28}'.format(mark + ' ' + user.first_name + ' ' + user.last_name),
              '{:.<17}'.format(user.phone), '{:.<21}'.format(user.email), '{:>10}'.format(user.password))

    print('\n\n|', '=' * 25, ' NEW APPLICANTS REPORT ', '=' * 25, '|',
          '\n| type/first/last name ----- phone number ----'
          ' email address ------- password |\n|', ' ' * 75, '|')
    for user in users_inventory:
        flag = True
        for account in accounts_inventory:
            if user.password == account.owner:
                flag = True
                break
            else:
                flag = False
        if not flag:
            print_user_list()
    new_account()


def account_update():
    """ Updates account's detail """
    # updates_inventory = []
    now = datetime.now()
    dt_string = now.strftime(" %d/%m/%Y %H:%M:%S ")

    def print_acc_details():
        print('\n', '=' * 45, '\n', 'Account N: ', '{:<34}'.format(account.account_id), '\n', '-' * 45,
              '\n 1. Account balance:    ', '{:{width}.{prec}f}'.format(account.balance, width=18, prec=2), 'lv.'
                                                                                                            '\n 2. Interest per month: ',
              '{:{width}.{prec}f}'.format(account.interest, width=18, prec=2), '%.')
        if type(account) is not DepositAccount:
            print(' 3. Pay per month: ', '{:{width}.{prec}f}'.format(account.pay_per_month, width=23, prec=2), 'lv.')
        print(' 4. Account password: ', '{:>23}'.format(account.owner), '\n 5. Quit.\n', '-' * 45)

    command = input('\nEnter Account Number:\t')
    for account in accounts_inventory:
        if account.account_id == command:
            acc_id = account.account_id
            old_detail = None
            new_detail = None
            print_acc_details()
            command = input('Enter one of the options above:\t')
            if command == '5':
                break
            if command == '1':
                old_detail = account.balance
                new_detail = float(input('Enter new balance:\t'))
                account.balance = new_detail
            if command == '2':
                old_detail = account.interest
                new_detail = float(input('Enter new interest:\t'))
                account.interest = new_detail
            if command == '3':
                old_detail = account.pay_per_month
                new_detail = float(input('Enter new pay per month:\t'))
                account.pay_per_month = new_detail
            if command == '4':
                old_detail = account.owner
                new_detail = input("Enter new owner's password:\t")
                account.owner = new_detail
            updates_inventory.append(AccountUpdate(acc_id, old_detail, new_detail, dt_string))
            print(f'\n Update successfully completed!')
            print_acc_details()
            print(f' Update recorded on: {dt_string}\n', '=' * 45, '\n\n')
    with open('updates_inventory', 'wb') as updates_inventory_file:
        pickle.dump(updates_inventory, updates_inventory_file)
    with open('accounts_inventory', 'wb') as accounts_inventory_file:
        pickle.dump(accounts_inventory, accounts_inventory_file)


def admin_main_screen():
    print('\n', '=' * 40, '\n', '*' * 8, 'ADMIN OPERATIONS MODE', '*' * 8,
          '\n\n 10. Accounts.'
          '\n 11. Users.'
          '\n 12. Transfers.'
          '\n 13. Updates Report'
          '\n 14. Quit.'
          '\n Please, enter one of the options above:\t', '\n', '-' * 40)


def staff_main_screen():
    print('\n', '=' * 40, '\n', '*' * 6, 'EMPLOYEE OPERATIONS MODE', '*' * 6,
          '\n\n 6. Open New User Account.'
          '\n 7. View Accounts.'
          '\n 8. View Transfers.'
          '\n 9. Quit.'
          '\n Please, enter one of the options above:\t', '\n', '-' * 40)


def user_main_screen():
    print('\n1. Money Transfer.'
          '\n2. Reports.'
          '\n3. Open New Account.'
          '\n4. Manage Profile.'
          '\n5. Quit.'
          '\nPlease, enter one of the options above:\t', '\n', '-' * 40)


def user_login():
    """ Access to user's accounts and main operations. """
    now = datetime.now()
    dt_string = now.strftime(" %d/%m/%Y %H:%M:%S ")

    command1 = input('\nPlease, enter your email:\t')
    command2 = input('\nPlease, enter your password:\t')
    flag = False
    for user in users_inventory:
        if command1 != user.email and command2 != user.password:
            pass
        if command1 == user.email and command2 == user.password:
            flag = True
            if command1.split('@')[1] == 'bestbank.eu':
                command = input('Would you like proceed as customer (Y):\t').upper()
                if command != 'Y':
                    if command2[-5::] == 'admin':
                        admin_main_screen()
                    elif command2[-5::] == 'staff':
                        staff_main_screen()
                    continue
            print('\n', '=' * 6, dt_string, '=' * 6,
                  f'\n Hello {user.first_name} {user.last_name},'
                  f'\n Welcome in Best Bank online system!'
                  f'\n\n Your Accounts:')
            print(' Acc.N:___type___Balance:')

            for account in accounts_inventory:
                if account.owner == user.password:
                    if type(account) is DepositAccount:
                        mark = 'Deposit:'
                    else:
                        mark = 'Credit:'
                    print(f' {account.account_id} {mark} {account.balance:.2f} lv.')
            user_main_screen()
    if not flag:
        print('\nInvalid username and/or password!\n', '-' * 32)


def all_accounts():
    """ Displays accounts reports and charts in different views """
    now = datetime.now()
    dt_string = now.strftime(" %d/%m/%Y at %H:%M:%S ")

    def print_head():
        print('\n', '=' * 47, '\nACCOUNTS REPORT: {:>30}'.format(dt_string),
              '\nacc.N: ----- balance <=>type ------ name ------')

    def print_accounts_report():
        print('{:.6}'.format(account.account_id), '{:.>15}'.format(account.balance),
              '{:.<5}'.format(mark), '{:.>19}'.format(user.first_name + ' ' + user.last_name))

    command = input('\n 1. Total.'
                    '\n 2. By Types + Charts.'
                    '\n 3. By Users.'
                    '\n 4. Single account'
                    '\n 5. <= Back'                    
                    '\n\nEnter one of the options above:\t')
    if command == '1':
        print_head()
        total_debit = 0
        total_credit = 0
        for account in accounts_inventory:
            for user in users_inventory:
                if user.password == account.owner:
                    if type(account) is DepositAccount:
                        total_debit += account.balance
                        mark = '<=Dt'
                    else:
                        total_credit += account.balance
                        mark = '=>Ct'
                    print_accounts_report()
        print('-' * 43, '\nTotal Debit:', '{:.>26}'.format(total_debit), ' lv.'
              '\nTotal Credit:','{:.>25}'.format(total_credit), ' lv.\n', '=' * 47, '\n')

    if command == '2':
        print_head()
        print('Deposit Accounts:')
        total_personal_deposits = 0
        total_business_deposits = 0
        total_staff_deposits = 0
        total_deposit = 0
        for account in accounts_inventory:
            if type(account) is DepositAccount:
                total_deposit += account.balance
                mark = '<=Dt'
                for user in users_inventory:
                    if user.password == account.owner:
                        if type(user) is Person:
                            total_personal_deposits += account.balance
                        if type(user) is Company:
                            total_business_deposits += account.balance
                        if isinstance(user, Staff):
                            total_staff_deposits += account.balance
                        print_accounts_report()
        print(f'Total: ....... {total_deposit} Debit\n', '-' * 47)

        print('Credit Accounts:')
        total_personal_credits = 0
        total_business_credits = 0
        total_staff_credits = 0
        total_credit = 0
        for account in accounts_inventory:
            if type(account) is CreditAccount:
                total_credit += account.balance
                mark = '=>Ct'
                for user in users_inventory:
                    if user.password == account.owner:
                        if type(user) is Person:
                            total_personal_credits += account.balance
                        if type(user) is Company:
                            total_business_credits += account.balance
                        if isinstance(user, Staff):
                            total_staff_credits += account.balance
                        print_accounts_report()
        print(f'Total: ....... {total_credit} Credit\n', '-' * 47)

        print('Mortgage Accounts:')
        total_personal_mrtgs = 0
        total_business_mrtgs = 0
        total_staff_mrtgs = 0
        total_mrtg = 0
        for account in accounts_inventory:
            if type(account) is MortgageAccount:
                total_mrtg += account.balance
                mark = '=>Ct'
                for user in users_inventory:
                    if user.password == account.owner:
                        if type(user) is Person:
                            total_personal_mrtgs += account.balance
                        if type(user) is Company:
                            total_business_mrtgs += account.balance
                        if isinstance(user, Staff):
                            total_staff_mrtgs += account.balance
                        print_accounts_report()
        print(f'Total: ...... {total_mrtg} Credit\n', '=' * 47, '\n\n')

        chart_command = input('\n  Structure By Types Users '
                              '\n 1. - Deposit '
                              '\n 2. - Credit.'
                              '\n 3. - Mortgage.'
                              '\n 4. Totals By Types Accounts.'
                              '\n 5. <= Back'
                              '\n\n For Account Structure Chart'
                              '\n please enter one of options above:\t')
        while chart_command in ['1', '2', '3', '4']:
            if command == '':
                break
            if chart_command == '1':
                a = total_personal_deposits
                b = total_business_deposits
                c = total_staff_deposits
                slices = [a, b, c]
                types = (f'personal\n{a:.0f}', f'business\n{b:.0f}', f'staff\n{c:.0f}')
                cols = ['c', 'r', 'g']
                plt.pie(slices, labels=types, colors=cols,
                        autopct='%1.1f%%')
                plt.title(f'Deposit Accounts Structure\non{dt_string}')
                plt.show()
            if chart_command == '2':
                a = total_personal_credits
                b = total_business_credits
                c = total_staff_credits
                slices = [a, b, c]
                types = (f'personal\n{a:.0f}', f'business\n{b:.0f}', f'staff\n{c:.0f}')
                cols = ['c', 'r', 'g']
                plt.pie(slices, labels=types, colors=cols,
                        autopct='%1.1f%%')
                plt.title(f'Credit Accounts Structure\non{dt_string}')
                plt.show()
            if chart_command == '3':
                a = total_personal_mrtgs
                b = total_business_mrtgs
                c = total_staff_mrtgs
                slices = [a, b, c]
                types = (f'personal\n{a:.0f}', f'business\n{b:.0f}', f'staff\n{c:.0f}')
                cols = ['c', 'r', 'g']
                plt.pie(slices, labels=types, colors=cols,
                        autopct='%1.1f%%')
                plt.title(f'Mortgage Accounts Structure\non{dt_string}')
                plt.show()
            if chart_command == '4':
                x = ['Deposits', 'Credits', 'Mortgages']
                y = [total_deposit, total_credit, total_mrtg]
                plt.bar(x, y, color='b')
                plt.title('Report By Type Accounts')
                plt.show()
            chart_command = input()

    if command == '3':
        applicants_list = []
        for user in users_inventory:
            for account in accounts_inventory:
                if user.password != account.owner:
                    continue
                else:
                    applicants_list.append(user)
                    break
        for user in users_inventory:
            if user not in applicants_list:
                continue
            print(f'\n{user.first_name} {user.last_name}:')
            total = 0
            for account in accounts_inventory:
                if account.owner == user.password:
                    print('{:.<6}'.format(account.account_id), '{:.>15}'.format(account.balance))
                    if account.account_id[0] == '1':
                        total += account.balance
                    else:
                        total -= account.balance
            print('Total:', '{:.>15}'.format(total))

    if command == '4':
        account_id = input('\n Enter account number:\t')
        mark = None
        for account in accounts_inventory:
            if account.account_id == account_id:
                if type(account) is DepositAccount:
                    mark = 'Deposit'
                if type(account) is CreditAccount:
                    mark = 'Credit'
                if type(account) is MortgageAccount:
                    mark = 'Mortgage'
                print(f'\n Account N:     {account_id}'
                      f'\n Type:         {mark}'
                      f'\n Balance:  {account.balance:.2f} lv'
                      f'\n Interest:      {account.interest:.2f} %')
                if type(account) is not DepositAccount:
                    print(f' Pay per month: {account.pay_per_month:.2f} lv.')


def transfer():
    """ Deposit to all accounts and withdraw from deposit accounts """
    # transactions_inventory = []
    def print_acc_balance():
        if type(account) is DepositAccount:
            mark = 'Deposit:'
        else:
            mark = 'Credit:'
        print(f' {account.account_id} {mark} {account.balance:.2f} lv.')

    password = input('\n Enter password:\t')
    now = datetime.now()
    dt_string = now.strftime(" %d/%m/%Y %H:%M:%S ")

    type_transfer = input('\n 1. Internal.'
                          '\n 2. Deposit.'
                          '\n 3. Withdraw.'
                          '\n Enter type of transfer:\t')
    account_id = input('\n Enter the account number:\t')
    amount = float(input("\n Enter the amount you would like to transfer:\t "))
    date_time = dt_string
    if type_transfer == '1':
        account2 = input('\n Enter the second account:\t')
        new_balance1 = 0
        new_balance2 = 0
        account1 = 0
        for account in accounts_inventory:
            if account.account_id == account_id and type(account) is DepositAccount:
                account.balance -= amount
                new_balance1 = account.balance
                transactions_inventory.append(Withdraw(account_id, amount, date_time))
            if account.account_id == account2:
                password = account.owner
                account1 = account_id
                account_id = account2
                if type(account) is DepositAccount:
                    account.balance += amount
                else:
                    account.balance -= amount
                new_balance2 = account.balance
                transactions_inventory.append(Deposit(account_id, amount, date_time))
        print('\n', '=' * 35, f'\n Internal transfer {amount:.2f} lv'
                              f'\n from acc.N:{account1} to acc.N:{account2}'
                              f'\n Recorded on:{dt_string}\n', '-' * 35,
              '\n New Balance:')
        print(' Acc.N:___type___Balance:')
        for account in accounts_inventory:
            if account.account_id == account1:
                print_acc_balance()
            if account.account_id == account2:
                print_acc_balance()
    else:
        mark = None
        for account in accounts_inventory:
            if account.account_id == account_id:
                password = account.owner
                if type_transfer == '2':
                    mark = 'Deposit'
                    if type(account) is DepositAccount:
                        account.balance += amount
                    else:
                        account.balance -= amount
                    transactions_inventory.append(Deposit(account_id, amount, date_time))
                if type_transfer == '3':
                    mark = 'Withdraw'
                    if type(account) is DepositAccount:
                        account.balance -= amount
                        transactions_inventory.append(Withdraw(account_id, amount, date_time))
                print('\n', '=' * 40, f'\n {mark} transfer {amount} lv.'
                                      f'\n acc.N:{account_id} New Balance: {account.balance:.2f} lv.'
                                      f'\n Recorded on:{dt_string}\n', '-' * 40)
        print(' Acc.N:___type___Balance:')
        for account in accounts_inventory:
            if account.owner == password:
                print_acc_balance()

    with open('transactions_inventory', 'wb') as transactions_inventory_file:
        pickle.dump(transactions_inventory, transactions_inventory_file)
    with open('accounts_inventory', 'wb') as accounts_inventory_file:
        pickle.dump(accounts_inventory, accounts_inventory_file)


def all_transactions():
    """ Displays transaction records in all accounts"""
    now = datetime.now()
    dt_string = now.strftime(" %d/%m/%Y at %H:%M:%S ")

    def print_report():
        print(' {:<6}'.format(transaction.account_id), ':', '{:.>12}'.format(transaction.amount),
              f'lv. {mark}', '{:.>25}'.format(transaction.date_time))

    command = input('\n 1. Total.'
                    '\n 2. Daily + Chart.'
                    '\n 3. <= Back.'
                    '\n Enter one of the options above:\t')
    if command == '1':
        total_deposit = 0
        total_credit = 0
        print('\n\n', '=' * 18, 'ALL TRANSFERS REPORT', '=' * 17, '\nacc.N:',
              '...... amount <==> type ......... date ... time', '\n', '-' * 57)
        for transaction in transactions_inventory:
            for account in accounts_inventory:
                if transaction.account_id == account.account_id:
                    if type(transaction) is Deposit:
                        mark = '<= Dt.'
                        total_deposit += transaction.amount
                        print_report()
                    else:
                        mark = '=> Ct.'
                        total_credit += transaction.amount
                        print_report()
        print('-' * 58, f'\n Total Dt: {total_deposit:.2f} lv.     '
                        f' Total Ct: {total_credit:.2f} lv.',
              '\n', '-' * 57, '\n Report done on:', dt_string, '\n')

    if command == '2':
        print('\n','='*8,'TOTAL DAILY TRANSFERS','='*8,
              '\n --- date ----- deposits ----- withdraws')
        tday = None
        total_deposit = 0
        total_credit = 0
        deposit_tday = 0
        credit_tday = 0
        X = []
        Y = []
        Z = []
        for transaction in transactions_inventory:
            if type(transaction) is Deposit:
                total_deposit += transaction.amount
            else:
                total_credit += transaction.amount
            if tday is None:
                tday = transaction.date_time[0:11]
                # X.append(tday)
                if type(transaction) is Deposit:
                    deposit_tday = transaction.amount
                else:
                    credit_tday = transaction.amount
            elif tday == transaction.date_time[0:11]:
                if type(transaction) is Deposit:
                    deposit_tday += transaction.amount
                else:
                    credit_tday += transaction.amount
                continue
            else:
                print(' {:<12}'.format(tday),
                      '{:{width}.{prec}f}'.format(deposit_tday, width=10, prec=2),
                      '{:{width}.{prec}f}'.format(credit_tday, width=15, prec=2))
                X.append(tday[0:6])
                Y.append(deposit_tday)
                Z.append(credit_tday)
                tday = transaction.date_time[0:11]
                if type(transaction) is Deposit:
                    deposit_tday = transaction.amount
                    credit_tday = 0
                else:
                    credit_tday = transaction.amount
                    deposit_tday = 0
        X.append(tday[0:6])
        Y.append(deposit_tday)
        Z.append(credit_tday)
        print(' {:<12}'.format(tday),
              '{:{width}.{prec}f}'.format(deposit_tday, width=10, prec=2),
              '{:{width}.{prec}f}'.format(credit_tday, width=15, prec=2))
        print('-'*40, f'\n Total:      {total_deposit:.2f} lv.  '
                      f'{total_credit:.2f} lv.\n', '-'*40)
        _X = np.arange(len(X))
        plt.title(f'D A I L Y   T R A N S F E R S\nreported on:{dt_string}')
        plt.bar(_X - 0.2, Y, 0.4)
        plt.bar(_X + 0.2, Z, 0.4)
        plt.xlabel('Days')
        plt.ylabel('amounts')
        plt.legend(['Deposit','Withdraw'], loc="upper left")
        plt.xticks(_X, X)
        chart = input('\nEnter to show in chart')
        if chart == '':
            plt.show()


def transfer_update():
    now = datetime.now()
    dt_string = now.strftime(" %d/%m/%Y at %H:%M:%S ")

    def print_transfer_details():
        print('\n Money Transfer:', transfer_time,
              '\n 1. Account N: ', transaction.account_id,
              f'\n 2. Amount: {transaction.amount:.2f} lv.')

    transfer_time = input('\n Enter date_time:\t')
    for transaction in transactions_inventory:
        if transfer_time == transaction.date_time[1:-1]:
            acc_id = transaction.account_id
            old_detail = None
            new_detail = None
            print_transfer_details()
            command = input(' 3. Quit.\n Enter one of the options above:\t')
            if command == '3':
                break
            if command == '1':
                old_detail = transaction.account_id
                new_detail = input('\n Enter new account:\t')
                transaction.account_id = new_detail
            if command == '2':
                old_detail = transaction.amount
                new_detail = float(input('\n Enter new amount:\t'))
                transaction.amount = new_detail
            updates_inventory.append(TransferUpdate(acc_id, old_detail, new_detail, dt_string))
            print('\n','='*45,'\n Update successfully completed!')
            print_transfer_details()
            print(f' Update recorded on: {dt_string}\n', '-' * 45, '\n\n')
    with open('updates_inventory', 'wb') as updates_inventory_file:
        pickle.dump(updates_inventory, updates_inventory_file)
    with open('transactions_inventory', 'wb') as transactions_inventory_file:
        pickle.dump(transactions_inventory, transactions_inventory_file)


def my_reports():
    """ """
    now = datetime.now()
    dt_string = now.strftime(" %d/%m/%Y at %H:%M:%S ")

    command = input('\n Enter password:\t')
    flag = None
    for user in users_inventory:
        if user.password != command:
            flag = True
            pass
        if user.password == command:
            flag = None
            break
    if flag:
        print('\n Invalid Password!')
        exit()
    print("\n 1. User's Balance."
          "\n 2. All Accounts Transfers."
          '\n 3. Single Account Transfers')
    command1 = input('    Enter one of the options above:\t')

    if command1 == '1':
        print('\n Acc.N:___type___Balance:')
        for account in accounts_inventory:
            if account.owner == command:
                if type(account) is DepositAccount:
                    mark = 'Deposit:'
                else:
                    mark = 'Credit:'
                print(f' {account.account_id} {mark} {account.balance:.2f} lv.')

    elif command1 == '2':
        my_accounts_list = []
        for account in accounts_inventory:
            if account.owner == command:
                my_accounts_list.append(account.account_id)
        for user in users_inventory:
            if user.password == command:
                print(f"\n{user.first_name} {user.last_name}'s   Money   Transfers   Report:")
                break
        total_debit = 0
        total_credit = 0
        print('=' * 60, '\n', 'acc.N:', '...... amount <==> type ......... date ... time ...', '\n', '-' * 60)
        for x in my_accounts_list:
            for transaction in transactions_inventory:
                if x == transaction.account_id:
                    if type(transaction) is Deposit:
                        total_debit += transaction.amount
                        print(' {:<6}'.format(transaction.account_id), ':', '{:.>12}'.format(transaction.amount),
                              'lv. <= Dt', '{:.>25}'.format(transaction.date_time))
                    else:
                        total_credit += transaction.amount
                        print(' {:<6}'.format(transaction.account_id), ':', '{:.>12}'.format(transaction.amount),
                              'lv. => Ct', '{:.>25}'.format(transaction.date_time))
        print(' ', '-' * 60, f'\n Total:      Dt:{total_debit:.2f}lv.       Ct:{total_credit:.2f}lv.\n', '=' * 60)

    elif command1 == '3':
        account1 = input('\nEnter account number:\t')
        print(f'\nAccount:{account1} Transactions Report:')
        print('=' * 60, '\n', 'acc.N:', '...... amount <==> type ............. date time', '\n', '-' * 60)
        total_debit = 0
        total_credit = 0
        for transaction in transactions_inventory:
            if account1 == transaction.account_id:
                if type(transaction) is Deposit:
                    total_debit += transaction.amount
                    print(' {:<6}'.format(transaction.account_id), ':', '{:.>12}'.format(transaction.amount),
                          'lv. <= Dt', '{:.>25}'.format(transaction.date_time))
                else:
                    total_credit += transaction.amount
                    print(' {:<6}'.format(transaction.account_id), ':', '{:.>12}'.format(transaction.amount),
                          'lv. => Ct', '{:.>25}'.format(transaction.date_time))
        print(' ', '-' * 60, f'\n Total:      Dt:{total_debit:.2f}lv.       Ct:{total_credit:.2f}lv.\n', '=' * 60)
    else:
        print('Invalid Number!')


def interest_calculator():
    """" Calculate interest and balance for period of months"""

    def print_scedule():
        if command == '1':
            print('{:>4}'.format(month),'{:{width}.{prec}f}'.format(interest_amount, width=8, prec=2),
                  '{:{width}.{prec}f}'.format(pay_per_month, width=10, prec=2),
                  '{:{width}.{prec}f}'.format(balance, width=15, prec=2))
        else:
            print('{:>4}'.format(month), '{:{width}.{prec}f}'.format(balance, width=15, prec=2),
                  '{:{width}.{prec}f}'.format(interest_amount, width=8, prec=2),
                  '{:{width}.{prec}f}'.format(pay_per_month, width=10, prec=2))

    command = input('\n 1. Deposit.'
                    '\n 2. Credit.'
                    '\n 3. Mortgage.'
                    '\n   Enter type account from above\t')

    type = input('\n 1. Person.'
                 '\n 2. Business.'
                 "\n   Enter client's type from above:\t")

    open_balance = float(input('\n Enter the beginning amount:\t'))
    if command == '1':
        pay_per_month = float(input(' Enter deposit per month:\t'))
    else:
        pay_per_month = None
    interest = float(input(' Enter percentage interest per month:\t'))
    period = int(input(' Enter number of months:\t'))
    balance = open_balance
    month = None
    interest_amount = None

    if command == '1':
        print('\n', '======= DEPOSIT ACCOUNT SCHEDULE ======='
                    '\n month   interest   pay       balance \n')

        for month in range(1, period + 1):
            interest_amount = balance * interest / 100
            if balance < 1000:
                interest_amount = 0
            balance = balance + interest_amount + pay_per_month
            print_scedule()
        print('\n', '=' * 8, 'DEPOSIT SCHEDULE SUMMARY', '=' * 8,
              f'\n If you open {open_balance:.2f} lv.Deposit Account'
              f'\n and you add {pay_per_month:.2f} lv. per month,'
              f'\n after {period} months you will have {balance:.2f} lv '
              f'\n in your account. Thank you!\n', '=' * 42)

    if command == '2':
        if period > 36:
            print("\n Sorry! Invalid Period.")
            exit()
        if (type == '1' and open_balance > 10000) or (type == '2' and open_balance > 100000):
            print("\n Sorry! Invalid Credit Amount.")
            exit()
        print('\n', '======= CREDIT ACCOUNT SCHEDULE ======='
                    '\nmonth      balance   interest      pay \n')

        for month in range(1, period + 1):
            pay_per_month = open_balance / period
            interest_amount = balance * interest / 100
            if type == '1' and month <= 3:
                interest_amount = 0
            if type == '2' and month <= 2:
                interest_amount = 0
            pay_per_month += interest_amount
            print_scedule()
            balance = balance - pay_per_month + interest_amount

    if command == '3':
        period_discount = None
        discount_interest = None
        credit = open_balance
        months = period
        principal_per_month: float = credit / months

        sum_pay1 = 0
        if type == '1':
            period_discount = 6
            discount_interest = 0
        if type == '2':
            period_discount = 12
            discount_interest = interest * 0.5
        amount = credit
        pay = 0
        for month in range(1, period_discount + 1):
            interest_per_month = amount * discount_interest / 100
            pay = principal_per_month + interest_per_month
            sum_pay1 += pay
            amount -= principal_per_month
        print('\n', '========= MORTGAGE ACCOUNT SCHEDULE ========='
                    '\nmonth balance   principal  interest      pay\n')
        amount = credit
        pay = sum_pay1 / period_discount
        for month in range(1, period_discount + 1):
            interest_per_month = amount * discount_interest / 100
            principal_per_month = pay - interest_per_month
            print('{:>4}'.format(month), '{:{width}.{prec}f}'.format(amount, width=10, prec=2),
                  '{:{width}.{prec}f}'.format(principal_per_month, width=8, prec=2),
                  '{:{width}.{prec}f}'.format(interest_per_month, width=8, prec=2),
                  '{:{width}.{prec}f}'.format(pay, width=10, prec=2))
            amount -= principal_per_month

        months2 = months - period_discount
        r1 = int(amount / months2)
        r2 = int(r1 + amount * interest / 100)
        amount2 = amount

        for pay_per_month in range(r1, r2):
            amount2 = amount
            count = 0
            for _ in range(months2):
                ppm = pay_per_month - amount2 * interest / 100
                amount2 -= ppm
                count += 1
                if amount2 <= 0:
                    break
            if amount2 <= 0:
                break

        for month in range(period_discount + 1, months):
            interest_per_month = amount * interest / 100
            principal_per_month = pay_per_month - interest_per_month
            print('{:>4}'.format(month), '{:{width}.{prec}f}'.format(amount, width=10, prec=2),
                  '{:{width}.{prec}f}'.format(principal_per_month, width=8, prec=2),
                  '{:{width}.{prec}f}'.format(interest_per_month, width=8, prec=2),
                  '{:{width}.{prec}f}'.format(pay_per_month, width=10, prec=2))
            amount -= principal_per_month
        interest_per_month = amount * interest / 100
        print(f' {months}    {amount:.2f}     0.00'
              f'     {interest_per_month:.2f}    '
              f'{(amount + interest_per_month):.2f}'
              '\n', '-' * 45)

        print('\n', '=' * 10, ' MORTGAGE SCHEDULE SUMMARY: ', '=' * 10,
              f'\n For total {open_balance:.2f} lv. in period of {months} months,'
              f'\n you will pay in first {period_discount} months: {pay:.2f} lv/mo,'
              f'\n then in next {months - period_discount - 1} months you will pay: {pay_per_month:.2f} lv/mo'
              f'\n and in a last month you will pay {(amount + interest_per_month):.2f} lv.'
              '\n Thank you!\n', '-' * 50)


def updates_report():
    """ Admin gets all updates records"""
    # updates_inventory = []
    now = datetime.now()
    dt_string = now.strftime(" %d/%m/%Y at %H:%M:%S ")

    print('\n', '{:*^60}'.format(' UPDATES REPORT '))
    print(' Accounts Updates:')
    for account in updates_inventory:
        if type(account) is AccountUpdate:
            print('{:15}'.format(account.acc_id), '{:>12}'.format(account.old_detail),
                  '{:>12}'.format(account.new_detail), '{:25}'.format(account.date_time))
    print('-' * 60)
    print(' Transfers Updates:')
    for update in updates_inventory:
        if isinstance(update, TransferUpdate):
            if not update.old_detail or not update.new_detail:
                continue
            print('{:15}'.format(update.acc_id), '{:>12}'.format(update.old_detail),
                  '{:>12}'.format(update.new_detail), '{:25}'.format(update.date_time))
    print('-' * 60)
    print('\n Profiles Updates:')
    for user in updates_inventory:
        if type(user) is UserUpdate:
            print('{:15}'.format(user.user_name), '{:>12}'.format(user.old_detail),
                  '{:>12}'.format(user.new_detail), '{:25}'.format(user.date_time))
    print('-' * 60, '\n', 'All updates done to:', dt_string)


def admin_users():
    command = input('\n 1. All Users List.'
                    '\n 2. One User Transfers.'
                    '\n 3. User Update.'
                    '\n 4. <= Back.'
                    '\n Enter one of the options above:\t')
    if command == '1':
        all_users_list()
    if command == '2':
        my_reports()
    if command == '3':
        user_update()


def admin_accounts():
    command = input('\n 1. All Accounts.'
                    '\n 2. Open New Account.'
                    '\n 3. Account Update.'
                    '\n 4. <= Back.'
                    '\n Enter one of the options above:\t')
    if command == '1':
        all_accounts()
    if command == '2':
        new_account()
    if command == '3':
        account_update()


def admin_transfers():
    command = input('\n 1. All Transfers.'
                    '\n 2. Money Transfer'
                    '\n 3. Transfer Update.'
                    '\n 4. <= Back.'
                    '\n Enter one of the options above:\t')
    if command == '1':
        all_transactions()
    if command == '2':
        transfer()
    if command == '3':
        transfer_update()
