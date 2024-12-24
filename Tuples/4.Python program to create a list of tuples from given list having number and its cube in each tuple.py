list_inputs=list(map(int,input().split()))
print(list_inputs)
output=[]
for i in list_inputs:
    output.append((i,i**3))
print(output)