input_string = list(map(str, input("Enter the string: ").split()))
vowels = {'a', 'e', 'i', 'o', 'u'}
output = ""
invalid = ""

for item in input_string:
    if vowels.issubset(set(item.lower())):
        output += item + " "
    else:
        invalid += item + ", "

# Print the valid and invalid outputs
print("Words containing all vowels:", output.strip())
print("Words without all vowels:", invalid.strip(", "))
