def check_longest_prefix(input_list):
    if not input_list:
        return ""
    prefix_ref=input_list[0]

    for item in input_list[1:]:
        while not item.startswith(prefix_ref):
            prefix_ref=item[:-1]
            if not prefix_ref:
                return ""
    return prefix_ref

input_strings=list(map(str,input("Enter the string:").split()))
print(check_longest_prefix(input_strings))

