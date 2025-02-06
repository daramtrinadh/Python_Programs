A=eval(input("Enter First Tuple:"))
B=eval(input("Enter First Tuple:"))
output=[(A[i],B[j]) for i in range(0,len(A)) for j in range(0,len(B))]
print("All pairs combinations",output)
# for i in range(0,len(A)):
#     for j in range(0,len(B)):
#         print(A[i],B[j])
# Enter first tuple: (1, 2, 3)
# Enter second tuple: (4, 5)