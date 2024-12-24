def longest_word(input_words):
    longest = input_words[0]
    for word in input_words:
        if len(word) > len(longest):
            longest = word
    return longest



input_words = list(map(str, input("Enter the words using comma separated: ").split(",")))
print("The longest word is:", longest_word(input_words))
