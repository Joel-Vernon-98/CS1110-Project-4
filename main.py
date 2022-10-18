import program_module as pm

file_prefix = input("Enter a file prefix: ")
old_file_name = f"{file_prefix}_old.txt"
new_file_name = f"{file_prefix}_new.txt"

try:
    with open(old_file_name, "r") as old_file, open(new_file_name, "w") as new_file:
        for line in old_file:
            account_number = pm.get_account_number(line)
            account_balance = pm.get_account_balance(line)
            customer_name = pm.get_customer_name(line).strip("\n")
            print(f"Verifying input: {account_number} {account_balance:10} {customer_name}")
            while True:
                transaction_code = pm.get_transaction_code()
                if transaction_code == "a":
                    new_line = pm.customer_file_entry(account_number, account_balance, customer_name)
                    print(f"New balance: {account_number} {account_balance} {customer_name}")
                    new_file.write(new_line)
                    break
                elif transaction_code == "w":
                    while True:
                        try:
                            account_balance = pm.withdraw_funds(account_balance,
                                                                pm.get_transaction_amount("withdrawal"))
                            break
                        except ValueError as err:
                            print(err)
                elif transaction_code == "d":
                    while True:
                        try:
                            account_balance = pm.deposit_funds(account_balance,
                                                               pm.get_transaction_amount("deposit"))
                            break
                        except ValueError as err:
                            print(err)
                elif transaction_code == "c":
                    if account_balance == 0:
                        print("Account is closed.")
                        old_file_line = old_file.readline().strip("\n")
                        break
                    else:
                        print("Account not closed because money is still in it.")
                else:
                    print(f"Entered an invalid command {transaction_code}")
        new_file.write("999999")


except FileNotFoundError:
    print(f"The file name {old_file_name} does not exist.")
