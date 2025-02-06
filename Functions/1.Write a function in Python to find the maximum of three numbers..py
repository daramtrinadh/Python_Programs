def max_num(numbers):
    initial_number=numbers[0]
    for i in range(1,len(numbers)):
        if numbers[i]>initial_number:
            initial_number=numbers[i]
    return initial_number


first_number=int(input("Enter The first Number:"))
second_number=int(input("Enter The second Number:"))
third_number=int(input("Enter The Third Number:"))
print(max_num([first_number,second_number,third_number]))