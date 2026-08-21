while True:
    n=input('enter a number or type Quit')
    if(n=='Quit'):
        print('congratulations you have break the infinite loop ')
        break
    elif (float(n)>=0):
        print('positive')
    elif (float(n)<0):
        print("negative")
    else:
        print('you have entered a wrong input')
    