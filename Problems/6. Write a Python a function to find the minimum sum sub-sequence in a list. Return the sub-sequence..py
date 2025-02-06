def sum_of_array(sub_array):
    total_sum = 0
    for item in sub_array:
        total_sum += item
    return total_sum

def max_sub_sequence(input_list):
    min_sum = float('inf')
    min_sub_array = []

    sub_arrays = []
    for i in range(0, len(input_list)):
        for j in range(i + 1, len(input_list) + 1):
            sub_arrays.append(input_list[i:j])

    for sub_array in sub_arrays:
        current_sum = sum_of_array(sub_array)
        if current_sum < min_sum:
            min_sum = current_sum
            min_sub_array = sub_array


    return min_sub_array, min_sum

input_list = [1,2,4,-1,-1,-2,8,2,-1,-6,2]
result = max_sub_sequence(input_list)
print(f"Sub-array with minimum sum: {result[0]}")
print(f"Minimum sum: {result[1]}")
