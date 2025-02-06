sample_list=[100,24,5,34,455,34]
n=len(sample_list)
#descending
#ascending

# print(sorted(sample_list))
for i in range(len(sample_list)):
    for j in range(0,n-i-1):
        if sample_list[j]>sample_list[j+1]:
            sample_list[j],sample_list[j+1]=sample_list[j+1],sample_list[j]
print(sample_list)