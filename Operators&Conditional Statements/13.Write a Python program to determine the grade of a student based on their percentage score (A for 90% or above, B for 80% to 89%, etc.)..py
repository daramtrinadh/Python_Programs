input_percentage = float(input("Enter the Percentage:"))

if input_percentage>100:
    print("Invalid Percentage")
elif input_percentage >= 90:
    print("Grade: A")
elif 80 <= input_percentage < 90:
    print("Grade: B")
elif 70 <= input_percentage < 80:
    print("Grade: C")
elif 60 <= input_percentage < 70:
    print("Grade: D")
else:
    print("Grade: F # FAIL 🤣")
