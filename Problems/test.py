# 5. Write a program that:
# •	Accepts a list of integers from the user
# •	Adds an element to the list
# •	Removes an element from the list
# •	Modifies an element at a specified index
# •	Performs an addition operation on two elements at user-specified indices and prints the sum

my_list=list(map(int,input().split()))
# adding element to list
my_list.append(8)
#remove element to list
my_list.remove(5)

#Modifies an element at a specified index
index_to_modify=int(input("Enter the index to modify:"))
new_value=int(input("Enter the new Value:"))
if 0 <= index_to_modify < len(my_list):
    my_list[index_to_modify] = new_value
    print("List after modifying:", my_list)
else:
    print("Invalid index.")
#Performs an addition operation on two elements at user-specified indices and prints the sum
first_index=int(input("Enter First index:"))
second_index=int(input("Enter the second Index:"))
if 0<=first_index<len(my_list) and 0<=second_index<len(my_list):
    print(my_list[first_index] + my_list[second_index])
#
print(my_list)
my_tuple = (1, 2, 3, 4, 5)
my_list = list(my_tuple)
print("List from tuple:", my_list)

my_list[2] = 10
print("Modified list:", my_list)

my_tuple = tuple(my_list)
print("Tuple from modified list:", my_tuple)

index1 = int(input("Enter the first index for addition: "))
index2 = int(input("Enter the second index for addition: "))
if 0 <= index1 < len(my_tuple) and 0 <= index2 < len(my_tuple):
    sum_of_elements = my_tuple[index1] + my_tuple[index2]
    print(f"Sum of elements at indices {index1} and {index2}: {sum_of_elements}")
else:
    print("Invalid indices.")
