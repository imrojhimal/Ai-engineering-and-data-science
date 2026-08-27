list1=[1,2,2,2,8,6,6,3,4,5]
s=set()
s1=set()
for val in list1:
    if val in s:
        s1.add(val)
    else:
        s.add(val)
print(f'the duplicates are {s1}')
