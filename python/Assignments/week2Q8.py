def calculator(a,b,op):
    if (op=='+'):
        return a+b
    elif(op=='*'):
        return a*b
    elif(op=='-'):
        return a-b
    elif(op=='/'):
        return a/b
    else:
        print('enterd a wrong input')
        return 0
op=input('welcome to the calculator choose an operation and enter +,*,-,/')
a,b=input('enter two numbers: ').split()
a=float(a)
b=float(b)
ans=print(calculator(a,b,op))
