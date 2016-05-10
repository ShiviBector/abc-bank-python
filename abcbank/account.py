from abcbank.transaction import Transaction
from datetime import datetime, timedelta

CHECKING = 0
SAVINGS = 1
MAXI_SAVINGS = 2
transactionDate=0

class Account:
    def __init__(self, accountType, balance=0.0):
        self.accountType = accountType
        self.transactions = []
        self.balance=balance
        
    def deposit(self, amount):
        if (amount <= 0):
            raise ValueError("amount must be greater than zero")
        else:
            self.transactions.append(Transaction(amount))

    def withdraw(self, amount):
        if amount> self.balance:
            raise ValueError(" Amount is greater than account balance")
        if (amount <= 0):
            raise ValueError("amount must be greater than zero")
        else:
            self.transactions.append(Transaction(-amount))
            transactionDate=datetime.now()
   
    def balance(self):
        return self.balance
        
    def interestEarned(self):
        amount = self.sumTransactions()
        if self.accountType == SAVINGS:
            if (amount <= 1000):
                return amount * (0.001/365)
            else:
                return 1 + (amount - 1000) * (0.002/365)
        if self.accountType == MAXI_SAVINGS:
            check_day=transactionDate-timedelta(10)
            if check_day != transactionDate :
                return amount * (0.05/365)
            else:
                return amount * (0.001/365)
        
    def sumTransactions(self, checkAllTransactions=True):
        return sum([t.amount for t in self.transactions])
        
    def transfer_between_accounts( self, target_account, amount):
        if (amount<=0):
            raise ValueError("Amount must be greater than zero")
        elif (amount>=self.balance):
            raise ValueError("Amount is greater")
        else:
            self.balance -= amount
            target_account.balance += amount
