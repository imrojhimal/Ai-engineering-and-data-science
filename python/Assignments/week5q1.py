class BankAccount:
    owner="jannatul ferdous khushbo"
    account=101
    def __init__(self,balance):
        self.balance=balance
    def deposit(self,newbalance):
        self.balance+=newbalance
    def withdraw(self,withdrew):
        self.balance-=withdrew
    def show(self):
        print(f"{self.owner} account number {self.account} \n has {self.balance} bdt")
b=BankAccount(1000)
b.deposit(500)
b.withdraw(820)
b.show()
        
