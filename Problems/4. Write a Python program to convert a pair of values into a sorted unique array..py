def sorted_unique_array(list_1,list_2):
    return set(list_1) | (set(list_2))

list_1=list(map(int,input("Enter the first pair numbers:").split()))
list_2=list(map(int,input("Enter the second pair numbers:").split()))
print(sorted_unique_array(list_1,list_2))