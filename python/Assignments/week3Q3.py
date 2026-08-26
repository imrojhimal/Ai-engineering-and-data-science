tup=(1,2,3,4,5,6,7,8,9)
even=[]
odd=[]
for val in tup:
    if(val%2==0):
        even.append(val)
    else:
        odd.append(val)
ev=(even)
od=(odd)
print(f'even tuples{ev}\nodd tuples {od}')