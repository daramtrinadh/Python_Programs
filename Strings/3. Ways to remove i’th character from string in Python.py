input_string=input("Enter the String:")
i=int(input("Enter the i'th value:"))

# 1st way
print(input_string[:i]+input_string[i+1:])

# 2nd way
output=""
for index in range(len(input_string)):
    if index!=i:
        output+=input_string[index]
print(output)



