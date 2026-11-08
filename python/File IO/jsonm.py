import json
with open("python/File IO/data.json","r") as f:
    pyobj=json.load(f)
    print(pyobj)
data={
    1:"orange",
    2:"apple",
    3:"tomato"
    }
with open("python/File IO/data.json","w") as f:
    newjsonstring=json.dump(data,f)
