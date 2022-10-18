FIRST_ACCOUNT_NUMBER, LAST_ACCOUNT_NUMBER = 100_000, 999_998
ACCOUNT_NUMBER_SENTINEL = 999_999
MINIMUM_ACCOUNT_BALANCE, MAXIMUM_ACCOUNT_BALANCE = 0.00, 9_999_999.99


def get_number(line: str) -> str:
    return line[:6]


def get_balance(line: str) -> float:
    return float(line[7:17].lstrip(" "))


def get_name(line: str) -> str:
    return line[18:]


def process_transaction(transaction_type: str, balance: float, transaction_amount: float) -> float:
    if transaction_type == "w":
        balance -= transaction_amount
        if balance < 0:
            raise ValueError("Error: This withdrawal amount will put your account below the minimum balance.")
        return balance
    else:
        balance += transaction_amount
        if balance > 9_999_999.99:
            raise ValueError("Error: This deposit amount will put your account over the maximum balance.")
        return balance


def get_transaction_amount(text: str) -> float:
    while True:
        transaction_amount = input(f"Enter a {text} amount: ")
        if not is_float(transaction_amount):
            print("INVALID INPUT: Please enter a numeric value.")
        elif float(transaction_amount) < 0:
            print("INVALID INPUT: Please enter a numeric value greater than 0.")
        else:
            return float(transaction_amount)


def is_float(num: str) -> bool:
    try:
        float(num)
        return True
    except ValueError:
        return False


def file_entry_string(account_number: str, balance: float, name: str) -> str:
    return f"{account_number} {balance:10.2f} {name}\n"


def get_transaction_code() -> str:
    while True:
        transaction_code = input("Enter a command (a,c,d,w): ")
        if transaction_code.lower() in ("a", "c", "d", "w"):
            break
        else:
            print(f"Entered an invalid command code {transaction_code}")
    return transaction_code.lower()



