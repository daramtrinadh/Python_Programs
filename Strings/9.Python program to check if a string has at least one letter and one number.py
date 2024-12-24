input_string=input("Enter the string:")
is_number=any(char.isdigit() for char in input_string)
is_alpha=any(char.isalpha() for char in input_string)
if is_number & is_alpha:
    print("Valid String")
elif not is_alpha:
    print("Please include at least one alphabet")
elif not is_number:
    print("Please include at least one number")
