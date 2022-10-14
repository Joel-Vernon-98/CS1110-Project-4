FIRST_ACCOUNT_NUMBER, LAST_ACCOUNT_NUMBER = 100_000, 999_998
ACCOUNT_NUMBER_SENTINEL = 999_999
MINIMUM_ACCOUNT_BALANCE, MAXIMUM_ACCOUNT_BALANCE = 0.00, 9_999_999.99


def get_account_number(line):
    return int(line[:6])


def get_account_balance(line):
    return float(line[7:17].lstrip(" "))


def get_customer_name(line):
    return line[18:]


def withdraw_funds(balance, withdrawal_amount):
    balance -= withdrawal_amount
    if balance < 0.00:
        raise ValueError("Error: Insufficient funds for withdrawal.")
    return balance


def deposit_funds(balance, deposit_amount):
    balance += deposit_amount
    if balance > 9_999_999.99:
        raise ValueError("Error: This deposit will put your account over the maximum allowed balance.")
    return balance


def customer_file_entry(account_number, account_balance, customer_name):
    return f"{account_number} {account_balance:10.2f} {customer_name}"

