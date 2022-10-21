import project_4_module as pm
from constants import SENTINEL


def main():
    file_prefix = input("Enter a file prefix: ")
    old_file_name = f"{file_prefix}_old.txt"
    new_file_name = f"{file_prefix}_new.txt"

    try:
        with open(old_file_name, "r") as old_file, open(new_file_name, "w") as new_file:
            file_line = old_file.readline().strip("\n")

    except FileNotFoundError:
        print(f"The file name {old_file_name} does not exist.")

    else:
        while file_line != SENTINEL:
            account_number = pm.get_number(file_line)
            account_balance = pm.get_balance(file_line)
            customer_name = pm.get_name(file_line)
            print(f"Verifying input: {account_number} {account_balance} {customer_name}")

            performing_transactions = True
            while performing_transactions:

                transaction_code = pm.get_transaction_code()
                if transaction_code == "a":
                    new_line = f"{pm.file_entry_string(account_number, account_balance, customer_name)}"
                    new_file.write(f"{new_line}\n")
                    print(f"New balance: {new_line}")
                    break

                elif transaction_code == "c":
                    if pm.account_is_closable(account_balance):
                        print("Account is closed")
                        break
                    print("Account not closed because money is still in it.")

                elif transaction_code == "w":
                    withdrawal_amount = input("Enter withdrawal amount: ")
                    while not pm.transaction_amount_is_valid(withdrawal_amount):
                        withdrawal_amount = input("Enter withdrawal amount: ")
                    account_balance = pm.process_transaction(transaction_code, account_balance,
                                                             float(withdrawal_amount))
                elif transaction_code == "d":
                    deposit_amount = input("Enter deposit amount: ")
                    while not pm.transaction_amount_is_valid(deposit_amount):
                        deposit_amount = input("Enter deposit amount: ")
                    account_balance = pm.process_transaction(transaction_code, account_balance,
                                                             float(deposit_amount))

                else:
                    print(f"Entered an invalid command {transaction_code}")

            file_line = old_file.readline().strip("\n")
        new_file.write(SENTINEL)
        print(f"\n{new_file_name} created successfully.")


if __name__ == "__main__":
    main()
