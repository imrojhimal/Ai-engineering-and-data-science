class product:
    count=0
    def __init__(self,name,price):
        self.name=name
        self.price=price
        product.count+=1
    @classmethod
    def productcount(cls):
        print(f'total number of product is {cls.count}')
    @staticmethod
    def discount(price,discount):
        finalprice=price-((discount*price)/100)
        return finalprice
p1=product('biscuits',100)
p2=product('chips',50)
p3=product('bread',600)
p4=product('cake',3000)
product.productcount()
    