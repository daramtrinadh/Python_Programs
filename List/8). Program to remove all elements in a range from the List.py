start,end=list(map(int,input("Enter the range:").split()))
sample_list=[1,2,4,56,7,89]
for i in sample_list[start:end+1]:
    sample_list.remove(sample_list[start])
print(sample_list)
