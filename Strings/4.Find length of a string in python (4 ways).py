input_string=input("Enter The string:")
print("1st way",len(input_string))

len_of_string=0
for i in input_string:
    len_of_string+=1
print("2nd way",len_of_string)

print("3rd way",input_string.__len__())