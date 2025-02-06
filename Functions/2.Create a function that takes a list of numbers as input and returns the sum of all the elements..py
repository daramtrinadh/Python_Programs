def max_sum_list(input_list):
    initial_sum=0
    for i in input_list:
        initial_sum+=i
    return initial_sum

input_list=list(map(int,input("Enter numbers in list:").split()))
print(max_sum_list(input_list))