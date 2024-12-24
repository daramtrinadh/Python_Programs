input_dict= {'A': [1, 2, 3, 4], 'B': [10, 15, 20], 'C': [7, 8, 9]}
for key,value in input_dict.items():
    filtered_values=[item for item in value if item%2==0 ]
    input_dict[key]=filtered_values
print(input_dict)
