def sorted_list_of_tuple(input_list):
    input_list.sort(key=lambda x: x[-1])
    return input_list

input_list_of_tuples=eval(input("Enter the list of tuples:"))
print(sorted_list_of_tuple(input_list_of_tuples))
# . Sample List : [(2, 5),(1, 2),(4, 4),(2, 3),(2, 1)]
# Expected Result : [(2, 1),(1, 2),(2, 3),(4, 4),(2, 5)]