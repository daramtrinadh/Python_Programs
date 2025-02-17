import re

result=re.match(r'hello','hello world')
if result:
    print("Match Found!")
else:
    print("No Match Found")