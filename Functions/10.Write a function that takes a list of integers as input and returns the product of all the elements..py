def product_numbers(input_list):
    product=1
    for i in input_list:
        product*=i
    return product

input_list=list(map(int,input("Enter the numbers:").split()))
print(product_numbers(input_list))
