def distinct_list(input_list):
    dist_list=set(input_list)
    return list(dist_list)

input_list=list(map(int,input("Enter the Numbers:").split()))
print(distinct_list(input_list))