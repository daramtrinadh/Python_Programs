def vowel_count(input_string):
    initial_count=0
    vowels={'a','e','i','o','u'}
    for i in input_string:
        if i.lower() in vowels:
            initial_count+=1
    return initial_count
input_string=input("Enter the string:")
print(vowel_count(input_string))