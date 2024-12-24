input_string=list(map(str,input("Enter the string:").split()))
output=""
for item in input_string:
    if len(item)%2==0:
        output+=item+" "
print(output)
