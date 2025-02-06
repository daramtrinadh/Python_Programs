sample_tuple=("apple",24,True)
List=["APPLE",48,False]
#tuple to list
convert_to_list=list(sample_tuple)
List.extend(convert_to_list)
#print(List)

#list to tuple

convert_to_tuple=tuple(List)
sample_tuple+=convert_to_tuple
print(sample_tuple)
