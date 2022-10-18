import program_module as pm

file_prefix = input("Enter a file prefix: ")
old_file_name = f"{file_prefix}_old.txt"
new_file_name = f"{file_prefix}_new.txt"

try:
    with open(old_file_name, "r") as old_file, open(new_file_name, "w") as new_file:

        loop_sentinel = "999999"
        file_line = old_file.readline().strip("\n")

        while file_line != loop_sentinel:
            account_number = pm.get_number(file_line)
            account_balance = pm.get_balance(file_line)
            customer_name = pm.get_name(file_line)
            print(f"Verifying input: {account_number} {account_balance} {customer_name}")

            while True:
                transaction_code = pm.get_transaction_code()
                if transaction_code == "a":
                    new_line = f"{pm.file_entry_string(account_number, account_balance, customer_name)}"
                    print(f"New balance: {new_line}")
                    new_file.write(f"{new_line}\n")
                    break

                elif transaction_code == "c":
                    if pm.account_is_closable(account_balance):
                        break

                elif transaction_code in ("w", "d"):
                    if transaction_code == "w":
                        transaction_amount = pm.get_transaction_amount("withdrawal")
                        account_balance = pm.process_transaction(transaction_code, account_balance, transaction_amount)
                    else:
                        transaction_amount = pm.get_transaction_amount("deposit")
                        account_balance = pm.process_transaction(transaction_code, account_balance, transaction_amount)

                else:
                    print(f"Entered an invalid command {transaction_code}")

            file_line = old_file.readline().strip("\n")
        new_file.write("999999")

except FileNotFoundError:
    print(f"The file name {old_file_name} does not exist.")
