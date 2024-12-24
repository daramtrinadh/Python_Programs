def checking_case(input_string):
    upperCase_count=0
    lowerCase_count=0
    for i in input_string:
        if i.islower():
            lowerCase_count+=1
        elif i.isupper():
            upperCase_count+=1
    return f"Uppercase Count:{upperCase_count},Lowercase Count:{lowerCase_count}"
input_string=input("Enter the String:")
print(checking_case(input_string))