input_tuple=tuple(map(int,input().split()))
K=int(input())
sorted_tuple=sorted(input_tuple)

print(f"K min values",sorted_tuple[:K])
print(f"k max values",sorted_tuple[-K:])
