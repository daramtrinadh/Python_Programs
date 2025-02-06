def check_longest_prefix(input_list):
    if not input_list:
        return ""
    prefix=""
    for chars in zip(*input_list):
        if len(set(chars))==1:
            prefix+=chars[0]
        else:
            break
    return prefix

input_strings=list(map(str,input("Enter the string:").split()))
print(check_longest_prefix(input_strings))

