import pytest

def factorial(num):
    if not isinstance(num,int) or num<0:
        raise ValueError("Number should be non integer value")
    result=1
    for i in range(2,num+1):
        result*=i
    return result

def test_positive_factorial():
    assert factorial(5)==120
    assert factorial(3)==6
def test_zero_factorial():
    assert factorial(0)==1
def test_one_factorial():
    assert factorial(1)==1
def test_unsupported_input():
    with pytest.raises(ValueError):
        factorial(-2)
    with pytest.raises(ValueError):
        factorial(2.4)
    with pytest.raises(ValueError):
        factorial("string")




# list_1=[1,2,3,4,5,6,7,8,9,10,11,12,13,16,17,18,19,20]
# for i in range(len(list_1)):
#     if i%3==0:
#         print(list_1[i])
# print(list_1[::3])


# tuple_list=[(1,2,3),(4,5,6,7),(8,9,10)]
# result=[]
# for tuple_item in tuple_list:
#     for item in tuple_item:
#         result.append(item)
# print(tuple(result))


# def product_items(input_list):
#     prod = 1
#     for i in input_list:
#         prod*=i
#     return prod
# input_list=list(map(int,input("Enter items:").split()))
# print(product_items(input_list))


# input_string=input("Enter The String:")
#
# for i in range(len(input_string)-1,-1,-1):
#     print(input_string[i],end="")

# list_1=["a","b","c","d"]
# list_2 =[1,2,3,4]
#
# result = {}
# for i in range(len(list_1)):
#     result[list_1[i]] = list_2[i]
# print(result)
# str_1="87trbov7ftewyf23rp378ry732ieesgdyuvwetkuy753674@#%%^#@#$$%%%$#85"
#
# str2 =" "
#
# for char in str_1:
#     if char.isalnum():
#         pass
#     else:
#         str2 += char
#
# print(str2)







