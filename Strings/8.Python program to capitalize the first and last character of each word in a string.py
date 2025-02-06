input_string=list(map(str,input("Enter the string:").split()))
output=""
for item in input_string:
    output+=item[0].upper()+item[1:len(item)].lower()+item[-1].upper()+" "
print(output)

