def sum(n):
   sum=0
   while n!=0:
       temp=n%10
       sum+=temp
       n=int(n/10)
   return sum
n=int(input('enter a number'))
print('total sum of the digits',sum(n))