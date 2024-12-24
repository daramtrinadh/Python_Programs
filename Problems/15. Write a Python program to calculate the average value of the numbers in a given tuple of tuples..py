input_tuple=((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))

output_list=[sum(item)/len(item) for item in input_tuple]
print(output_list)