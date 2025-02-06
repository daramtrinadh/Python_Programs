input_count=int(input("Enter How many numbers to compare:"))
output=0
for i in range(input_count):
    numb=int(input(f"Enter {i+1} number:"))
    if numb>output:
        output=numb
print(output)