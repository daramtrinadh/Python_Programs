def check_prime(num):
    if num<2:
        return False
    for j in range(2,int(num**0.5)+1):
        if num%j==0:
            return False
    return True
input_list=list(map(int,input("Enter the numbers:").split()))
are_all_prime=all(check_prime(i) for i in input_list)
print(are_all_prime)


