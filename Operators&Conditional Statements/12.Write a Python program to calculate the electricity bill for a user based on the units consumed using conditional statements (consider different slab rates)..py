def calculate_bill(units):
    if units <= 100:
        # First 100 units at 0.50 per unit
        bill = units * 0.50
    elif units <= 200:
        # Next 100 units (101 to 200) at 0.75 per unit
        bill = 100 * 0.50 + (units - 100) * 0.75
    elif units <= 300:
        # Next 100 units (201 to 300) at 1.00 per unit
        bill = 100 * 0.50 + 100 * 0.75 + (units - 200) * 1.00
    elif units <= 400:
        # Next 100 units (301 to 400) at 1.50 per unit
        bill = 100 * 0.50 + 100 * 0.75 + 100 * 1.00 + (units - 300) * 1.50
    else:
        # Above 400 units at 2.00 per unit
        bill = 100 * 0.50 + 100 * 0.75 + 100 * 1.00 + 100 * 1.50 + (units - 400) * 2.00

    return bill



units_consumed = float(input("Enter No of Units:"))

bill = calculate_bill(units_consumed)
print(f"The electricity bill for {units_consumed} units is: ${bill:.2f}")
