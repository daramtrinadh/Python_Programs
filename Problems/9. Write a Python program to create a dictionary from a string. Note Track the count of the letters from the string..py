input_string=input("Enter the String:")
count_letters={}
for i in input_string:
    if i in count_letters:
        count_letters[i]+=1
    else:
        count_letters[i]=1
print(count_letters)