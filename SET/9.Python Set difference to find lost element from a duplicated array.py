sample_array=[1, 2, 3, 4, 5, 2]
sample_set=set(sample_array)
lost_item=[item for item in sample_set if sample_array.count(item)>1 ]
print(lost_item)
