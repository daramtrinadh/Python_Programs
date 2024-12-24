input_list=list(map(int,input("Enter the numbers:").split()))
target=int(input("Enter the target:"))
subarrays=[]
for i in range(0, len(input_list)):
    for j in range(i + 1, len(input_list) + 1):
        if len(set((input_list[i:j]))) == 3 and sum(input_list[i:j]) == target:
            subarrays.append(input_list[i:j])

print(subarrays)

# [1, 2, -1, 0, -2, 3]