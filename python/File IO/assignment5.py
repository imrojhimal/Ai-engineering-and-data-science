try:
    with open("python/File IO/date.txt","r") as f:
     data=f.read()
     print(data)
except FileNotFoundError:
   print("File is not found!")