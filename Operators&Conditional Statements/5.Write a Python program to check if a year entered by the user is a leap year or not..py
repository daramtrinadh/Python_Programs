input_year=int(input("Enter the Year:"))
if input_year%4==0 & input_year%100==0 & input_year%400==0:
    print(f"Entered {input_year} is Leap Year")
elif not input_year%4==0:
    print("Entered Year is not a leap year")
elif not input_year%100==0:
    print("Entered Year is not a leap year")
elif not input_year%400==0:
    print("Entered Year is not a leap year")
