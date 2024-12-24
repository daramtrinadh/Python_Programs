input_list=list(map(int,input("Enter the numbers:").split()))
filtered_list=list(filter(lambda x:x%19==0 or x%13==0,input_list))
print(filtered_list)