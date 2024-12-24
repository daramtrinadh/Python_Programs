no_of_tuples=int(input("Enter No of tuples:"))
output=[]
for i in range(no_of_tuples):
    input_each_tuple=eval(input(f"Enter {i+1} tuple:"))
    [output.append(item) for item in input_each_tuple]
print(output)