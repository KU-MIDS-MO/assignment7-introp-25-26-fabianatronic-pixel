def make_account(initial_balance):
    if not isinstance (initial_balance, (int,float)) or initial_balance < 0:
        raise ValueError ("Initial balance must be a non-negativve number")
        
    balance = initial_balance
    
    def deposit (amount):
        nonlocal balance
        if not isinstance (amount, (int,float)) or amount <= 0:
            raise ValueError ("Deposit amount must be positive")
        balance += amount
        return balance
    
    def withdraw (amount):
        nonlocal balance
        if not isinstance (amount, (int,float)) or amount <=0:
           raise ValueError ("Withdrawal amount must be positive")
        if amount > balance:
           raise ValueError ("Insufficient funds")
        balance -= amount
        return balance
    
    return deposit, withdraw

    
