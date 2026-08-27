words=["banana","apple","orange","grape","kiwi","mango","pear","peach","plum","cherry"]
dic={}
print(type(dic))
for val in words:
    dic.update({val:len(val)})
print(dic)