input_string=input("Enter the string:")
first_half=input_string[:len(input_string)//2].upper()
print(first_half+input_string[len(input_string)//2:])