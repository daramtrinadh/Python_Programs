input_number = int(input("Enter the number:"))


if input_number <= 1:
    print(f"{input_number} is not a prime number")
else:
    for i in range(2, int(input_number**0.5) + 1):
        if input_number % i == 0:
            print(f"{input_number} is not a prime number")
            break
    else:
        print(f"{input_number} is a prime number")
