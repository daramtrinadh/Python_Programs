input_char=input("Enter the character:")
vowels={'a','e','i','o','u'}
if len(input_char)>1:
    print("Enter Single length character!!")
elif not input_char.isalpha():
    print("Enter Alphabet Character")
else :
    if input_char.lower() not in vowels:
        print(f"Entered Character {input_char} is Consonant")
    else:
        print(f"Entered Character {input_char} is Vowel")

