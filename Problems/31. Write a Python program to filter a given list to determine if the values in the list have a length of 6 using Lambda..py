input_list=list(map(int,input("Enter the Numbers:").split()))
filtered_list=list(filter(lambda x:len(x)==6,input_list))
print(filtered_list)