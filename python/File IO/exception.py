x=int(input("Enter a number: "))
try:
    ans=10/x
except ZeroDivisionError:
    print("you can't divide zero")
except ValueError:
    print("you have enter wrong input")
else:
    print(f"The result is {ans}")
