input_dict= {1: [2, 3, 4], 2: [5, 6], 3: [7, 8, 9, 10]}
for key,value in input_dict.items():
    sum_values=0
    for i in value:
        sum_values+=i
    input_dict[key]=sum_values
print(input_dict)

