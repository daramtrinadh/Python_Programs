input_sentence=list(map(str,input("Enter the sentence:").split()))
filter_list=list(filter(lambda x:len(x)>=4,input_sentence))
print(filter_list)
