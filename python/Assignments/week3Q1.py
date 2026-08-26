str=input("Enter a string: ")
start=0
end=len(str)-1
while start<end:
    if(str[start]==str[end]):
        start+=1
        end-=1
    else:
        print(f'{str} is not a palindrome')
        break
if(start>=end):
    print(f'{str} is a palindrome')
