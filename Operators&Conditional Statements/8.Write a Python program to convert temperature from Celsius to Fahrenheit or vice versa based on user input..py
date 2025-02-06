print("Enter 1 to calculate Fahrenheit and 2 for Celsius")
option = int(input("Enter Option 1 or 2:"))

if option == 1:
    input_Celsius = int(input("Enter Celsius:"))
    fahrenheit = (input_Celsius * 9/5) + 32
    print(f"Fahrenheit for {input_Celsius} Celsius is: {fahrenheit:.2f}°F")
elif option == 2:
    input_Fahrenheit = float(input("Enter Fahrenheit:"))
    celsius = (input_Fahrenheit - 32) * 5/9
    print(f"Celsius for {input_Fahrenheit} Fahrenheit is: {celsius:.2f}°C")
else:
    print("Invalid Option")
