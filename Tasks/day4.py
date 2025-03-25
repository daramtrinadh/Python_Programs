
# # 1. List and Tuple Methods
lst = [1, 2, 3, 4, 5]
lst.append(6)
print(lst)
lst.extend([7, 8])
print(lst)
lst.insert(2, 10)
print(lst)
lst.remove(10)
print(lst)
print(lst.pop())
print(lst.index(4))
print(lst.count(3))
lst.sort()
print(lst)
lst.reverse()
print(lst)
lst_copy = lst.copy()
print(lst_copy)
lst.clear()
print(lst)
#
tpl = (1, 2, 3, 4, 5)
print(tpl.count(2))
print(tpl.index(4))
#
# # 3. User-defined len() Function
def custom_len(iterable):
    count = 0
    for _ in iterable:
        count += 1
    return count

print(custom_len([1, 2, 3, 4]))

# 4. Check if Two Values Exist in a List
lst = list(map(int, input("Enter list elements: ").split()))
v1, v2 = map(int, input("Enter two values: ").split())
print(v1 in lst and v2 in lst)

# 5. User-defined Sort Function
def sort_ascending(numbers):
    ascending_list = []
    for num in numbers:
        inserted = False
        for j in range(len(ascending_list)):
            if num < ascending_list[j]:
                ascending_list.insert(j, num)
                inserted = True
                break
        if not inserted:
            ascending_list.append(num)
    return ascending_list
def sort_descending(numbers):
    descending_list = []
    for num in numbers:
        inserted = False
        for j in range(len(descending_list)):
            if num > descending_list[j]:
                descending_list.insert(j, num)
                inserted = True
                break
        if not inserted:
            descending_list.append(num)
    return descending_list


numbers_list = list(map(int, input("Enter the numbers: ").split()))
numbers_tuple=tuple(map(int,input("Enter the tuple numbers").split()))

print(sort_ascending(numbers_list))
print(sort_descending(numbers_list))
print(tuple(sort_ascending(list(numbers_tuple))))
print(tuple(sort_descending(list(numbers_tuple))))



# 6. Reverse List and Find Second Highest
def reverse_list(lst):
    return lst[::-1]

def second_highest(lst):
    return sorted(lst, reverse=True)[1]

lst = [10, 20, 5, 8, 15]
print(reverse_list(lst))
print(second_highest(lst))


# 7. Multiply 10 Digits by 2
nums = tuple(map(int,(input().split())))
result=tuple(num*2 for num in nums)
print(result)

# 8. Find Middle Element Without Predefined Functions
lst = list(map(int, input("Enter list: ").split()))
mid_index = len(lst) // 2
print(lst[mid_index])

# take two indexes as input from the user ex:1 and 10(last index) use them
# for list slicing print them with negative indexing ex: if it is 4th index -5 and if it is 10th index -1
# 9. List Slicing with Negative Indexing
# Taking input for the list
lst = list(map(int, input("Enter list: ").split()))
i1, i2 = map(int, input("Enter two indexes: ").split())
pos_slice = lst[i1:i2]
print(lst[-i1:-i2:-1])
neg_slice = lst[-i1:-i2:-1] if i1 > i2 else lst[-i1::-1]

# Printing the results
print("Positive Index Slicing:", pos_slice)
print("Negative Index Slicing (Reversed Order):", neg_slice)


# 13. Create a Loop for Automatic Duplicates
def auto_duplicate(value, n):
    lst = []
    for i in range(n):
        lst.append(value if i % 2 == 0 else i + 1)
    return lst

print(auto_duplicate(3, 10))


