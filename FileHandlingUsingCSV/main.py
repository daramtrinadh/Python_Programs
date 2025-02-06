import csv
# with open('industry.csv','w') as sample_csv:
#     row=['Trinadh',21,'Hyderabad','Engineer']
#     content=csv.writer(sample_csv)
#     content.writerow(row)
# with open('example.csv','w+') as example_csv:
#     field=['Name','Age','Stream']
#     rows=[['Trinadh','22','CSE'],['Ronaldo','39','Football'],["Ramos",'37','Hockey']]
#     file1=csv.writer(example_csv)
#     file1.writerow(field)
#     file1.writerows(rows)
#     example_csv.close()
# with open('example.csv','r+') as read_csv:
#     content=csv.DictReader(read_csv)
#     for line in content:
#         print(line['Name'],line['Stream'])

with open('example.csv', 'w+', newline='') as write_csv:
    data = [
        {'Name': 'Alice', 'Age': '30', 'City': 'New York', 'Occupation': 'Engineer'},
        {'Name': 'Bob', 'Age': '25', 'City': 'Los Angeles', 'Occupation': 'Designer'},
        {'Name': 'Charlie', 'Age': '35', 'City': 'Chicago', 'Occupation': 'Teacher'},
        {'Name': 'Diana', 'Age': '28', 'City': 'Houston', 'Occupation': 'Doctor'},
        {'Name': 'Eva', 'Age': '40', 'City': 'Miami', 'Occupation': 'Artist'}
    ]
    fieldnames=['Name','Age','City','Occupation']

    file1=csv.DictWriter(write_csv,fieldnames=fieldnames)
    file1.writeheader()
    file1.writerows(data)



