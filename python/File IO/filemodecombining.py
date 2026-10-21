f=open("python/File IO/data.txt","r+")
# if  you start reading the file first it will actually write from the last character cause it reads till the end
new=f.write("Hey you know about bangladesh")
print(f.read())
