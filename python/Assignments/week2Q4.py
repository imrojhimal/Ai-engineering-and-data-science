def sep(n):
   count=0
   while n!=0:
       temp=n%10
       count+=1
       n=int(n/10)
   return count
n=int(input('enter a number'))
print('total digits',sep(n))