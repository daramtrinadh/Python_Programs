input_list=list(map(int,input("Enter the numbers:").split()))
target=int(input("Enter the target:"))
subarrays=[]
for i in range(0, len(input_list)):
    for j in range(i + 1, len(input_list) + 1):
        print(input_list[i:j])
        if len(set((input_list[i:j]))) == 3 and sum(input_list[i:j]) == target:
            subarrays.append(input_list[i:j])

print(subarrays)

# [1, 2, -1, 0, -2, 3]

# input_list = [1, 2, -1, 0, -2,3]
# target = int(input("Enter the target: "))
#
# subarrays = []
#
#
# for i in range(len(input_list) - 2):
#     subarray = input_list[i:i + 3]  # Extract subarray of length 3
#     if sum(subarray) == target:
#         subarrays.append(subarray)
#
# # Display the results
# print("Valid subarrays of length 3 with the target sum:", subarrays)