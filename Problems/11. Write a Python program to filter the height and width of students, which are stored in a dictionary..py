input_dict= {'John': (170, 65), 'Alice': (160, 50), 'Bob': (180, 80), 'Charlie': (155, 45)}
# Filter Criteria: Height > 160 and Weight > 60
output={}
for key,value in input_dict.items():
    height,weight=value
    if int(height)>160 and int(weight)>60:
        output[key]=value
print(output)


