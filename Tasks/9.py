lst = list(map(int, input("Enter list: ").split()))
i1, i2 = map(int, input("Enter two indexes: ").split())
pos_slice = lst[i1:i2]
print(lst[-i1:-i2:-1])
neg_slice = lst[-i1:-i2:-1] if i1 > i2 else lst[-i1::-1]

# Printing the results
print("Positive Index Slicing:", pos_slice)
print("Negative Index Slicing (Reversed Order):", neg_slice)