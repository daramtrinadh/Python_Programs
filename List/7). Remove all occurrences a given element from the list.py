sample_list=[1,2,3,3,2,1]
sample_number=3

for item in sample_list[:]:
    if item==sample_number:
        sample_list.remove(sample_number)
print(sample_list)