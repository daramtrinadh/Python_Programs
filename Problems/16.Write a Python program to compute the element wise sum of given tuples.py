input_tuple=((1, 2, 3, 4),(3, 5, 2, 1),(2, 2, 3, 1))
output=()
for item in zip(*input_tuple):
    sum_of_values=sum(item)
    output+=(sum_of_values,)
print(output)