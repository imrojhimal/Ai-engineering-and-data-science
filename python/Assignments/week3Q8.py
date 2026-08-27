list1=[1,2,3,4]
list2=[4,5,6]
s1=set(list1)
s2=set(list2)
print(s1)
print(s2)
if(s1.intersection(s2)!=set()):
    print(f'here is the common value {s1.intersection(s2)}')
else:
    print('there is no common value exist')