a=int(input('enter a:'))
b=int(input('enterb:'))
end=max(a,b)
start=min(a,b)
for i in range(start,end+1):
    if i%2==0:
        print(i)