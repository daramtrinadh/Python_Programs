def find_roots(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if a==0:
        print("There are no roots")
    else:
        if discriminant > 0:
            root1 = (-b + (discriminant) ** 0.5) / (2 * a)
            root2 = (-b - (discriminant) ** 0.5) / (2 * a)
            print(f"The roots are real and distinct: {root1} and {root2}")
        elif discriminant == 0:
            root = -b / (2 * a)
            print(f"The root is real and repeated: {root}")
        else:
            real_part = -b / (2 * a)
            imaginary_part = (abs(discriminant)) ** 0.5 / (2 * a)
            print(f"The roots are complex: {real_part} + {imaginary_part}i and {real_part} - {imaginary_part}i")


a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))


find_roots(a, b, c)
