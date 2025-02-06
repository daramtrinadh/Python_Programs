dict_1 = {
    1: "apple",
    "name": "John",
    (2, 3): "tuple key"
}
keys=[]
values=[]
key_value_pairs=[]
for key,value in dict_1.items():
    keys.append(key)
    values.append(value)
    key_value_pairs.append((key,value))
print("Keys in dict_1:",keys)
print("values in dict_1:",values)
print("Key value pairs:",key_value_pairs)