def check_even_odd(number):
    if (number%2==0):
        return "Even Number"
    else:
        return "Odd Number"

input_number=int(input("Enter the number:"))
print(check_even_odd(input_number))