sq=[i*i for i in range(6) if i%2!=0]
print(sq)
nums=[-2,-1,-5,3,5,2,-9,-89]
nums=[0 if val<0 else val for val in nums]
print(nums)
words=["hi","hello","fuck","shiball","gaesikkiya"]
words=[val.upper() for val in words]
print(words)