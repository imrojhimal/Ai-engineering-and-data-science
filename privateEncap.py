class Bank:
    def __init__(self,balance):
        self.__balance=balance #protected variable
b=Bank(50000)
#print(b.__balance) not accessible 
print(b._Bank__balance)# accessing with data mangling
    