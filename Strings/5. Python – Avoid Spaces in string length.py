input_string=input("Enter the String:")
output=""

for i in input_string:
    if i!=" ":
        output+=i
print("Length of string avoiding spaces:",len(output),output)

