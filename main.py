# Import dependencies
import p4_module as pm

# Import constants
import constants as const


# Define main function
def main():
    # Get file name from user.
    file_prefix = input("Enter a file prefix: ")

    # Assign variables for original file name and for new file name
    old_file_name = f"{file_prefix}_old.txt"
    new_file_name = f"{file_prefix}_new.txt"

    # Try/Except to catch FileNotFound Error when attempting to read a file that does not exist.
    try:
        # Open original file and new file
        with open(old_file_name, "r") as old_file, open(new_file_name, "w") as new_file:
            end_of_file = const.SENTINEL
            file_line = old_file.readline().strip("\n")

            # while loop that runs until End of File is reached
            while file_line != end_of_file:
                # Assign each piece of account information to a variable
                account_number, account_balance = pm.get_number(file_line), pm.get_balance(file_line)
                customer_name = pm.get_name(file_line)
                print(f"Verifying input: {account_number} {account_balance} {customer_name}")

                # while loop that runs until the user is done preforming transactions on customer's account
                while True:
                    transaction_code = pm.get_transaction_code()
                    # Write updated customer data to new file after all transactions have been preformed and breaks loop
                    if transaction_code == "a":
                        new_line = f"{pm.file_entry_string(account_number, account_balance, customer_name)}"
                        print(f"New balance: {new_line}")
                        new_file.write(f"{new_line}\n")
                        break
                    elif transaction_code == "c":
                        # Breaks while loop without writing customer data to new file only if account balance = 0.00
                        if pm.account_is_closable(account_balance):
                            break
                    elif transaction_code in ("w", "d"):
                        # withdraw money from account if transaction_code is "w"
                        if transaction_code == "w":
                            transaction_amount = pm.get_transaction_amount("withdrawal")
                            account_balance = pm.process_transaction(transaction_code, account_balance,
                                                                     transaction_amount)
                        # otherwise deposit money if transaction code is "d"
                        else:
                            transaction_amount = pm.get_transaction_amount("deposit")
                            account_balance = pm.process_transaction(transaction_code, account_balance,
                                                                     transaction_amount)
                    # Print an error message if invalid transaction code is entered.
                    else:
                        print(f"Entered an invalid command {transaction_code}")
                # Read next line of old file
                file_line = old_file.readline().strip("\n")
            # Print sentinel at end of new file
            new_file.write("999999")

    except FileNotFoundError:
        print(f"The file name {old_file_name} does not exist.")
    # Print statement so user knows program finished running without any errors
    else:
        print(f"\n{new_file_name} created successfully.")


# Call main
main()
