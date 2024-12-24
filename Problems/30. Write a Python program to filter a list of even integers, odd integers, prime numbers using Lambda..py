def check_prime(x):
    if x<2:
        return False
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            return False
    return True
input_list=list(map(int,input("Enter the numbers:").split()))
even_numbers=list(filter(lambda x:x%2==0,input_list))
odd_numbers=list(filter(lambda x:x%2!=0,input_list))
prime_numbers=list(filter(lambda x:check_prime(x),input_list))
print(input_list)
print("Even Numbers:",even_numbers)
print("Odd Numbers:",odd_numbers)
print("Prime Numbers:",prime_numbers)