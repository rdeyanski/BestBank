from Bank.Functions import all_accounts, all_transactions, admin_main_screen,\
    welcome, user_login, register, transfer, my_reports, admin_transfers,\
    interest_calculator, user_main_screen, new_account, user_update,\
    staff_main_screen, new_user_account, admin_users, admin_accounts, updates_report

if __name__ == '__main__':
    while True:
        welcome()
        command = input()
        if command not in ['1', '2', '3']:
            break
        if command == '3':
            interest_calculator()
        if command == '2':
            register()
        if command == '1':
            user_login()
            command1 = input()
            while True:
                if command1 == '1':
                    transfer()
                    user_main_screen()
                    command1 = input()
                elif command1 == '2':
                    my_reports()
                    user_main_screen()
                    command1 = input()
                elif command1 == '3':
                    new_account()
                    user_main_screen()
                    command1 = input()
                elif command1 == '4':
                    user_update()
                    user_main_screen()
                    command1 = input()
                elif command1 == '6':
                    new_user_account()
                    staff_main_screen()
                    command1 = input()
                elif command1 == '7':
                    all_accounts()
                    staff_main_screen()
                    command1 = input()
                elif command1 == '8':
                    all_transactions()
                    staff_main_screen()
                    command1 = input()
                elif command1 == '10':
                    admin_accounts()
                    admin_main_screen()
                    command1 = input()
                elif command1 == '11':
                    admin_users()
                    admin_main_screen()
                    command1 = input()
                elif command1 == '12':
                    admin_transfers()
                    admin_main_screen()
                    command1 = input()
                elif command1 == '13':
                    updates_report()
                    admin_main_screen()
                    command1 = input()
                else:
                    break

        # if command == '4':
        #     all_accounts()






