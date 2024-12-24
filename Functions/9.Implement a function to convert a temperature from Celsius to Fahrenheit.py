def celsius_to_fahrenheit(celsius):
    fahrenheit=(celsius*9/5)+32
    return fahrenheit

input_celsius=float(input("Enter the celsius:"))
print(celsius_to_fahrenheit(input_celsius))