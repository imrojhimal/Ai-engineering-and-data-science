with open("python/File IO/names.txt","w") as  f:
    f.write("himal\nnahida\nkhushbu\ntahamina\nemon")

with open("python/File IO/names.txt","r") as  f:
    data=f.read()
    print(data)
