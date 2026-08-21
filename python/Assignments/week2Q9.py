def isprime(n):
    end=int((n/2)+1)
    if(n==2):
     print('damn prime')
     return
    if(n<2):
      print('non prime')
      return
    for i in range(2,end):
      if(n%i==0):
        print('yuup its a non prime number')
        return
    print('prime number')
n=int(input('enter any number you like '))
isprime(n)