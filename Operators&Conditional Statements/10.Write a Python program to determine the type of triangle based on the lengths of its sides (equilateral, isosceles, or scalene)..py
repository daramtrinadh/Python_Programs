side_1=int(input("Enter side_1 length:"))
side_2=int(input("Enter side_2 length:"))
side_3=int(input("Enter side_3 length:"))
if side_1==side_2==side_3:
    print("Equilateral Triangle")
elif side_1==side_2 or side_2==side_3 or side_1==side_3:
    print("Isosceles Triangle")
else:
    print("Scalene Triangle")