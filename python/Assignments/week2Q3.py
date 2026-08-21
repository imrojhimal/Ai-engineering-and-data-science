def sep(n):
   while n!=0:
       temp=n%10
       print(temp)
       n=int(n/10)
n=int(input('enter a number'))
sep(n)