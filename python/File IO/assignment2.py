with open("python/File IO/logs.txt","a") as f:
    f.write("\nprograms runs succesfully")
with open("python/File IO/logs.txt","r") as f:
    data=f.read()
    print(data)
