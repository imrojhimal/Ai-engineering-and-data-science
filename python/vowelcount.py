word="artificial education"
ans=0
count=0
for vow in word:
    if(vow=='a'or vow=='e'or vow=='o'or vow=='i'or vow=='u'):
        count+=1
    elif vow==' ':
        continue
    else:
        ans+=1
print('number of vowels: ',count)
print('number of consonants: ',ans)