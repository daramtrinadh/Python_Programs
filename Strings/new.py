str_1="aaaabbccccdd0011"
pairs={}
for i in str_1:
    if i in pairs:
        pairs[i]+=1
    else:
        pairs[i]=1
output=""
print(pairs)
for key,value in pairs.items():
    print(f"{value}{key}")
