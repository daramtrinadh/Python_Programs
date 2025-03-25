# # x=5
# # def func1():
# #
# #     global y
# #
# #
# # print(x+y)
# # sample_dict={"name":"Trinadh","name":"Praveen"}
# # print(sample_dict)
# # list_1=["a","b","c","d","e"]
# # list_2=[1,2,3,4,5]
# #
# # output={}
# # for i in range(len(list_1)):
# #     output[list_1[i]]=list_2[i]
# # print(output)

# # str_1="trinadh@07/-#982!"
# # str_2="trinadh@07/-#982!trinadh982!@07"
# # output=""
# # for i in str_1:
# #     if i.isalpha():
# #         output+=i
# # print(output)
# #
# # char_count={}
# # for i in str_2:
# #     if i in char_count:
# #         char_count[i]+=1
# #     else:
# #         char_count[i]=1
# # print(char_count)
#
# # def gen():
# #     yield "toy1"
# #     yield "toy2"
# #     yield "toy3"
# #
# # for i in gen():
# #     print(i)
#
# # list_1=[2,3,4,5]
# #
# # output=[]
# #
# # for i in range(len(list_1)):
# #     mul=1
# #     for j in range(0,len(list_1)):
# #         if list_1[i]==list_1[j]:
# #             pass
# #         else:
# #             mul*=list_1[j]
# #     output.append(mul)
# #
# # print(output)
#
# # list_1=["Trinadh/n","Praveen/n","Thundersoft/n"]
# # with open('sample.txt','w+') as sample_file:
# #     for line in list_1:
# #         sample_file.writelines(line)
#
# # with open('sample.txt','r') as new_file:
# #     content=new_file.readline()
# #     with open('newtext.txt','w+') as new_text_file:
# #         new_text_file.write(content)
# #         new_text_file.seek()
#
# class Car():
#     def details(self):
#         return "Car details"
#     def sound(self):
#         return "Main sound"
# class Toyota(Car):
#     def sound(self):
#         return "Toyota car sound"
#     def lights(self):
#         return "lights"
# class Buggati(Toyota):
#     def sound(self):
#         return "Buggati sound"
# class Shift(Buggati,Toyota,Car):
#     super().Car(details)
#     def __init__(self):
#
#     def window(self):
#         return "windows"
#
#
# shift=Shift()
# print(shift.details())
# print(shift.sound())
# print(shift.lights())
#
# #
# #
# # car=Car()
# # toyota=Toyota()
# # buggati=Buggati()
# # print(buggati.details())
# # print(car.sound())
# # print(toyota.sound())
#
#
# 1bucket 5 2ndbucket 3
# 1 bucket-0 2nd bucket 3 =>3
# 1st bucket -5 2nd bucket 0 =>5 3rd bucket -(3)8
# 1st bucket 2 2nd bucket 0 => 3rd bucket -3 (6)8
# 1st bucket 0 2nd bucket 2 =>3r bucket-6
#
#
# target=int(input("Enter the Target:"))
#
# def check_prime(n):
#     if n<2:
#         return False
#     for i in range(2,int(n**0.5)+1):
#         if n%i==0:
#             return False
#     return True
# # def check_sum():
#
# prime_nums=[]
# for num in range(1,target+1):
#     if check_prime(num):
#         prime_nums.append(num)
# found = False
# for i in range(len(prime_nums)):
#     for j in range(i+1, len(prime_nums)):
#         if prime_nums[i] + prime_nums[j] == target:
#             print(f"pair found: {prime_nums[i]}, {prime_nums[j]}")
#             found = True
#
# if not found:
#     print("No prime pair found.")

