from constants import ACCOUNT_BALANCE_START, ACCOUNT_BALANCE_END, ACCOUNT_NUMBER_END, CUSTOMER_NAME_START


def get_number(line: str) -> str:
    """Get customer's account number from line in formatted customer data file.

    Examples:
        >>> get_number("100789 5681745.99 Eich, Brendan")
        '100789'
        >>> get_number("650430    2398.12 Wall, Larry")
        '650430'

    Args:
        line (str): A line from the file being read.

    Returns:
        The account number as a string.
    """
    return line[:ACCOUNT_NUMBER_END]


def get_balance(line: str) -> float:
    """Get customer's account balance from line in formatted customer data file.

    Examples:
        >>> get_balance("100789 5681745.99 Eich, Brendan")
        5681745.99
        >>> get_balance("650430    2398.12 Wall, Larry")
        2398.12

    Args:
        line (str): A line from the file being read.

    Returns:
        The account balance as a float.
    """
    return float(line[ACCOUNT_BALANCE_START:ACCOUNT_BALANCE_END])


def get_name(line: str) -> str:
    """Get customer's name from line in formatted customer data file.

    Examples:
        >>> get_name("100789 5681745.99 Eich, Brendan")
        'Eich, Brendan'
        >>> get_name("650430    2398.12 Wall, Larry")
        'Wall, Larry'

    Args:
        line (str): A line from the file being read.

    Returns:
        Customer name as a string.
    """
    return line[CUSTOMER_NAME_START:]


def process_transaction(transaction_code: str, balance: float, transaction_amount: float) -> float:
    """Processes transactions and returns account balance.

    Examples:
        >>> process_transaction("w", 50.67, 40.00)
        10.67
        >>> process_transaction("d", 5.00, 15.00)
        20.0

    Args:
        transaction_code (str): Code to choose withdrawal/deposit.
        balance (float): Starting account balance.
        transaction_amount (float): Value of the transaction being performed.

    Returns:
        Resulting account balance as string
    """
    if transaction_code == "w":
        return round(balance - transaction_amount, 2)
    elif transaction_code == "d":
        return round(balance + transaction_amount, 2)


def transaction_amount_is_valid(transaction_amount: str) -> bool:
    """Checks if transaction amount user entered is valid.

    Examples:
        >>> transaction_amount_is_valid("-120.00")
        INVALID INPUT: Please enter a numeric value greater than 0.
        False
        >>> transaction_amount_is_valid("Hello.")
        INVALID INPUT: Please enter a numeric value.
        False
        >>> transaction_amount_is_valid("567.99")
        True

    Args:
        transaction_amount (str): The user entered transaction amount

    Returns:
        True if input is non-negative float, else False
    """
    try:
        transaction_amount = float(transaction_amount)
    except ValueError:
        print("INVALID INPUT: Please enter a numeric value.")
        return False
    else:
        if float(transaction_amount) <= 0.00:
            print("INVALID INPUT: Please enter a numeric value greater than 0.")
            return False
    return True


def get_transaction_code() -> str:
    """Ask the user for a transaction code until a valid input is entered.

    Returns:
        Valid transaction code as string.
    """
    valid_input = False
    while not valid_input:
        transaction_code = input("Enter a command (a,c,d,w): ")
        if transaction_code.lower() in ("a", "c", "d", "w"):
            return transaction_code.lower()
        print(f"Entered an invalid command {transaction_code}.")


def account_is_closable(balance: float) -> bool:
    """Checks if account is eligible to be closed and returns a boolean.

    Examples:
        >>> account_is_closable(19.89)
        False
        >>> account_is_closable(0.00)
        True

    Args:
        balance (float): The balance of the account.

    Returns:
        True if balance <= 0 else False.
    """
    if balance <= 0:
        return True
    return False


def file_entry_string(account_number: str, balance: float, name: str) -> str:
    """Converts customer data into formatted string to be written to new file and returns the string.

    Examples:
        >>> file_entry_string("100000", 43736.57, "Rossum, Guido V.")
        '100000   43736.57 Rossum, Guido V.'
        >>> file_entry_string("320056", 5.01, "Ritchi, Dennis MacAlistair.")
        '320056       5.01 Ritchi, Dennis MacAlistair.'

    Args:
        account_number (str): Customer's account number.
        balance (float): Customer's account balance.
        name (str): Customer's name.

    returns:
        Formatted string
    """
    return f"{account_number} {balance:10.2f} {name}"
