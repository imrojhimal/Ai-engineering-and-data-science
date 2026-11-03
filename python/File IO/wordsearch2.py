with open("python/File IO/data.txt","r") as f:
    count=1
    while True:
        data=f.readline()
        if "python" in data:
            print(f"found at line {count}")
            break
        else:
            count+=1
