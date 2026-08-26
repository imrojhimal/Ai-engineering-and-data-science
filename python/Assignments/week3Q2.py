list=[1,2,3,4,5,9]
length=len(list)-1
sum=0
while(0<=length):
    sum+=list[length]
    length-=1
avg=(sum/len(list))
print(f'the average is {avg}')