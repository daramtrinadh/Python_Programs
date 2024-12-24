def reverse(input_list,start_index):
    if start_index < 0 or start_index >= len(input_list):
        return "Start index is out of bounds."
    reverse_list=input_list[start_index:]
    modified_list=reverse_list[::-1]
    return input_list[:start_index]+modified_list

input_list=list(map(int,input("Enter the numbers:").split()))
start_index=int(input("Enter Start Range:"))

print(reverse(input_list,start_index))
