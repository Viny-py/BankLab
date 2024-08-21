import time

balance = 0
withdraw_counter = 3
withdraw_limit = 500
extract = str()
menu = '''
========================Vy Bank========================

[1] Deposit
[2] Withdraw
[3] Extract
[4] Leave

========================Vy Bank========================
'''

while True:
    option = input(menu)

    match option:
        case "1":
            amount = float(input("How much would you like to deposit? (0 to go back)\nR$"))
            if amount < 0:
                print("Unable to complete your deposit!\nYou cannot deposit a negative number!\n")
                continue
            elif amount == 0:
                continue
            else:
                print(f"Deposit of R${amount:.2f} was made!\n")
                balance += amount
                extract += f"Deposit of R${amount:.2f}\n"
                continue
        case "2":
            amount = float(input(f"How much would you like to withdraw? (0 to go back)\n(limit: R${withdraw_limit:.2f}) ({withdraw_counter} withdraws left)\nR$"))
            if amount == 0:
                continue            
            elif withdraw_counter <= 0:
                print("Unable to complete your withdraw!\nYou can only withdraw 3 times!\n")
                continue
            elif amount > withdraw_limit:
                print("Unable to complete your withdraw!\nYou cannot withdraw more than R$500.00!\n")
                continue
            else:
                if amount < 0:
                    print("Unable to complete your withdraw!\nYou cannot withdraw a negative number!\n")
                    continue
                elif amount > balance:
                    print(f"Unable to complete your withdraw!\nYou don't have R${amount:.2f} on your bank account to withdraw\n")
                    continue
                else:
                    print(f"You withdrew R${amount:.2f}!\n")
                    withdraw_counter -= 1
                    balance -= amount
                    extract += f"Withdraw of R${amount:.2f}\n"
                    continue
        case "3":
            print("========================EXTRACT========================\n\n")
            print("No Transactions were made!\n") if not extract else print(extract)
            print(f"\nBalance R${balance:.2f}")
            print("\n\n========================Vy Bank========================")
            time.sleep(3)
            continue
        case "4":
            print("\n\n\n\n\n\nThank you for using Vy Bank!\n\n\n\n\n\n")
            break
