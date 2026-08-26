info=[("alice",'math'),('bob','sci'),('cat','math'),
      ('tania','sci'),('khushbu','phy'),('nahida','phy')]
print(info)
s=set()
for val in range(len(info)):
    s.add(info[val][1])
print(s)