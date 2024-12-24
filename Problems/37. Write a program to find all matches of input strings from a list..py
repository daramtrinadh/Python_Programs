input_list=list(map(str,input("Enter the Strings:").split()))
find_string=str(input())
filtered_list=list(filter(lambda x:find_string.lower() in x ,input_list))
print(filtered_list)
