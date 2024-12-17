sample_list=[20,40,60,80]
#adding element
sample_list.append(100)
# print(sample_list)

#removing element
for item in sample_list:
    if item==100:
        sample_list.remove(item)
print(sample_list)

