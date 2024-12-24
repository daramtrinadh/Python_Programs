dict1 = {1: 10, 2: 20, 3: 30}
dict2 = {2: 40, 3: 50, 4: 60}
for key,value in dict2.items():
    if key in dict1:
        dict1[key]+=value
    else:
        dict1[key]=value
print(dict1)
