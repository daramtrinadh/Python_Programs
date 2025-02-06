def compare(list_1,list_2):
    if (set(list_1)) & (set(list_2)):
        return True
    else:
        return False
list_1=list(map(int,input("Enter the numbers:").split()))
list_2=list(map(int,input("Enter the Numbers:").split()))
print(compare(list_1,list_2))