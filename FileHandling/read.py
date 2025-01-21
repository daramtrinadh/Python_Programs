# import os
# import shutil
# with open('example.txt','w+') as file1:
#     lines=["Hello World\n","Welcome to python File Handling\n"]
#     file1.writelines(lines)
#     file1.seek(0)
#     content=file1.read()
#     print("Added lines in example.txt")
# with open('output.txt','w+') as file2:
#     lines=["This is a new file\n","Python means not snake\n"]
#     file2.writelines(lines)
#     file2_content=file2.read()
#     file2.close()
#     print("Added new file named output.txt")
#
# with open('output.txt','r') as appending_file:
#     for data in appending_file:
#         example_file=open('example.txt','a')
#         example_file.writelines(data)
#     appending_file.close()
#
# ##Checking File Existence
# try:
#     with open('temp.txt','r') as temp_file:
#         if temp_file:
#             content=temp_file.read()
#             print(content)
# except FileNotFoundError:
#     print("Given file is not there")
#
# ##delete file
# ##import os module
# file_path='temp.txt'
# if os.path.exists(file_path):
#     os.remove(file_path)
#     print("file path has been removed")
# else:
#     print("File does not exist")
#
# #count words lines of a file
# with open('output.txt','r+') as sample_file:
#     lines=0
#     words=0
#     characters=0
#     check_data=sample_file.readlines()
#     print(check_data)
#     for data in check_data:
#         print(data)
#         lines+=1
#         words+=len(data.split())
#         characters+=len(data)
# print("Lines:",lines)
# print("Words:",words)
# print("Characters:",characters)
#
# source_file='output'
# shutil.copytree(source_file,'copyfile')
#
# # Search and Replace python with javascript
# with open('output.txt',"r+") as sample_file:
#     content=sample_file.readlines()
#     sample_file.seek(0)
#     for data in content:
#         updated_lines=data.replace("Python","Javascript")
#         sample_file.write(updated_lines)
#
# #Merge two files output and example as merge file
# with open('merge.text','w+') as merge_file:
#     with open('example.txt', 'r') as example_file:
#         example_content = example_file.readlines()
#
#     with open('output.txt', 'r') as output_file:
#         output_content = output_file.readlines()
#     example_content.extend(output_content)
#     merge_file.writelines(example_content)
#
#
#


# with open('log.txt','r') as file1:
#     content=file1.readlines()
#     output={}
#     error_count=0
#     print(content)
#     for i in range(0, len(content)):
#         if "error" in content[i].lower():
#             output[i]=content[i]
#             error_count+=1
#     print(output)



# def palindrome(user_input):
#     first_half = user_input[:len(user_input) // 2].lower()
#     second_half = user_input[len(user_input) // 2 + 1:].lower()
#     track_len = 0
#     increase_index = -1
#     for i in range(0,len(first_half)):
#         if first_half[i]==second_half[increase_index]:
#             increase_index-=1
#             track_len+=1
#             pass
#         else:
#             return False
#     return track_len
#
# user_input=input("Enter the String:")
# output=(palindrome(user_input))
# if output==len(user_input)//2:
#     print("palindrome")
# else:
#     print("Not a palindrome")


# if user_input[::-1].lower()==user_input.lower():
#     print("Its Palindrome")
# else:
#     print("Not a palindrome")
