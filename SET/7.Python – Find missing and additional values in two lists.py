List_1=[1, 2, 3, 4]
List_2= [3, 4, 5, 6]

Missing_values=set(List_1)-set(List_2)
Additional_values=set(List_2)-set(List_1)
print(Missing_values)
print(Additional_values)
