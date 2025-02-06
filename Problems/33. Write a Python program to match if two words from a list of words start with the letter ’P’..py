input_list=list(map(str,input("Enter the Strings:").split()))
words_starting_with_p = [word for word in input_list if word[0].lower() == 'p']
if len(words_starting_with_p)>=2:
    print(words_starting_with_p)
else:
    print("There are no two matching strings with starting letter P")
