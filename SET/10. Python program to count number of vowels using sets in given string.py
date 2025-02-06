input_string=str(input("Enter String:"))
vowels={'a','e','i','o','u','A','E','I','O','U'}
expected_output={}
for i in input_string:
    if i in vowels:
        if i in expected_output:
            expected_output[i]+=1
        else:
            expected_output[i]=1
print(expected_output)