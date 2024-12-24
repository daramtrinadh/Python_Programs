input_number=int(input("Enter the number:"))
output=1
for i in range(1,input_number+1):
    output*=i
print(output)

#using recursion
def factorial(n):
    if n==0 | n==1:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(input_number))