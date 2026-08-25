marks=[10,20,50,90,120,1,178,36]
x=1
index=0
for val in marks:
    if(val==x):
        print(f'{x} found at index {index}')
        break
    index+=1
