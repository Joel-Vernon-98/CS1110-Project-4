# Import file of constant values
import constants as const


# Functions for parsing user data from file lines
def get_number(line: str) -> str:
    return line[:const.END_OF_ACCOUNT_NUMBER]


def get_balance(line: str) -> float:
    return float(line[const.START_OF_ACCOUNT_BALANCE:const.END_OF_ACCOUNT_BALANCE].lstrip(" "))


def get_name(line: str) -> str:
    return line[const.START_OF_CUSTOMER_NAME:]


# Functions for processing account transactions
def process_transaction(transaction_type: str, balance: float, transaction_amount: float) -> float:
    if transaction_type == "w":
        return balance - transaction_amount
    else:
        return balance + transaction_amount


def get_transaction_amount(text: str) -> float:
    while True:
        transaction_amount = input(f"Enter a {text} amount: ")
        if not is_float(transaction_amount):
            print("INVALID INPUT: Please enter a numeric value.")
        elif float(transaction_amount) < 0:
            print("INVALID INPUT: Please enter a numeric value greater than 0.")
        else:
            return float(transaction_amount)


def get_transaction_code() -> str:
    while True:
        transaction_code = input("Enter a command (a,c,d,w): ")
        if transaction_code.lower() in ("a", "c", "d", "w"):
            break
        else:
            print(f"Entered an invalid command {transaction_code}.")
    return transaction_code.lower()


# Helper functions for transaction processing
def account_is_closable(balance):
    if balance <= 0:
        print("Account is closed")
        return True
    print("Account not closed because money is still in it")
    return False


def is_float(num: str) -> bool:
    try:
        float(num)
        return True
    except ValueError:
        return False


# Function to format strings to write to new file
def file_entry_string(account_number: str, balance: float, name: str) -> str:
    return f"{account_number} {balance:10.2f} {name}"
