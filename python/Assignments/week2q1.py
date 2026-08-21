s=int(input('Enter your salary:'))
tax=0
if s<30000:
    tax=s*(5/100)
    net=s-tax
    print('your tax rate is 5% and net salary is',net)
elif (s>=30000 and s<70000):
    tax=s*(15/100)
    net=s-tax
    print('your tax rate is 15% and net salary is',net)
else:
    tax=s*(25/100)
    net=s-tax
    print('your tax rate is 25% and net salary is',net)