vowels_count=0
vowels={'a','i','e','o','u'}
string_input=input("enter the string:")
for i in string_input:
    if i.lower() in vowels:
        vowels_count+=1
print(vowels_count)