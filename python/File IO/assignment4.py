import json
with open("python/File IO/cities.json","r") as f:
    data=json.load(f)
    print(type(data),data)
city,population=input("Enter a new city and its population ").split()
data.update({city:population})
with open("python/File IO/cities.json","w") as f:
    newdata=json.dump(data,f)
