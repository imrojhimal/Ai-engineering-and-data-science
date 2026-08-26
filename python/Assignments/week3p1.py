info=[("alice",'math'),('bob','sci'),('cat','math'),
      ('tania','sci'),('khushbu','phy'),('nahida','phy')
      ,('tania','eng'),('khushbu','math'),('nahida','sci'),
      ("alice",'phy'),('bob','eng'),('cat','sci')]
s=set()
for val in range(len(info)):
    s.add(info[val][1])
for name,course in info:
    if(course=='sci'):
        print(name)
dict={}
for name,course in info:
    if(dict.get(name)==None):
        dict.update({name:set()})
        dict[name].add(course)
    else:
        dict[name].add(course)
print(dict)