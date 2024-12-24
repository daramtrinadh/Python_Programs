
num_terms = int(input("Enter the number of terms: "))


first, second = 0, 1
count = 0

print("Fibonacci series:")


while count < num_terms:
    print(first, end=" ")
    next_term = first + second
    first = second
    second = next_term
    count += 1
