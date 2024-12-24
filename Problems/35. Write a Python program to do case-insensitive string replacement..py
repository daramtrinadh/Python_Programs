def case_insensitive(input_list,find_string,replace_string):
    result=""
    for i in input_list:
        if i==find_string:
            result+=replace_string+" "
        else:
            result+=i+" "
    return result

input_list=list(map(str,input("Enter The Sentence:").split()))
find_string=str(input("Enter the String to replace:"))
replace_string=str(input("Enter the string to replace With:"))
print(case_insensitive(input_list,find_string,replace_string))
