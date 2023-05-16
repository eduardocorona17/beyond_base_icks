class BankAccount:
    def __init__(self, account_holder):
        # BankAccount methods can access self._balance but code outside
        # this class should not:
        self._balance = 0
        self._name = account_holder
        with open(self._name + 'Ledger.txt', 'w') as ledger_file:
            ledger_file.write('Balance is 0\n')

    def deposit(self, amount):
        if amount <= 0:
            return # Don't allow negative deposits.
        self._balance += amount
        with open(self._name + 'Ledger.txt', 'a') as ledger_file:
            ledger_file.write('Deposit ' + str(amount) + '\n')
            ledger_file.write('Balance is ' + str(self._balance) + '\n')

    def withdraw(self, amount):
        if self._balance < amount or amount < 0:
            return
        self._balance -= amount
        with open(self._name + 'Ledger.txt', 'a') as ledger_file:
            ledger_file.write('Withdraw ' + str(amount) + '\n') 
            ledger_file.write('Balance is ' + str(self._balance) + '\n')
acct = BankAccount('Alice') # Create account for ALice.
acct.deposit(120) # _balance can be affected through deposit()
acct.withdraw(40) # _balance can be affected through withdraw()
