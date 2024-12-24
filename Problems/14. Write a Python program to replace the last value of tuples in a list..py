input_tuple=[(10, 20, 40), (40, 50, 60), (70, 80, 90)]
output_list=[(item[:-1]+(100,)) for item in input_tuple]
print(output_list)
