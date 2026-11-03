with open("python/File IO/data.txt","r") as f:
    count=1
    ad=f
    for var in f:
        if "python" in var:  #python reads in line by line automatically in loop
            print(f"found at line {count}")
            break
        else:
            count+=1

