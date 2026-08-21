while True:
    n=int(input('enter a integer to guess'))
    if(n<77):
        print('too low')
    elif(n>77):
        print('too high')
    elif(n==77):
        print('bingo!')
        break
    else:
        print("something went wrong")