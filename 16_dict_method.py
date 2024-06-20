myDict = {
    "Fast": "I am Super Hero",
    "Yuvi": "He is a Hero",
    "anotherdic": {"Yuvi" : "Yuvi is Football Player"},
    1:2
}

print(list(myDict.keys())) # print list in dic 
print(type (myDict.keys())) # print type in dic 
print(myDict.keys())# print dict
print(myDict.values()) # print value in dic 
print(myDict.items()) # print value in dic 

# Update Dict above dic 
print(myDict) 
updateDict = {
    "Raja" : "He is Demon",
    "Divya" : "She is my GF"
}
myDict.update(updateDict)
print(myDict)


print(myDict.get("Diya")) 
print(myDict["Divya"]) 

print(myDict.get("Diya1")) # return none  if there is no  any element is dic 
print(myDict["Divya1"]) # throw error if tehre is no any element is dic


