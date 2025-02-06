input_range=int(input("Enter Range:"))
for i in range(1,input_range+1):
    print(i)
    for j in range(1,21):
        print(f"{i}x{j}={i*j}")


