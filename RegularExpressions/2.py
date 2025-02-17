import re
match=re.match(r'world','hello world')

if match:
    print("Found the match")
else:
    print("Not found the match")

search=re.search(r'world','hello world')
if search:
    print("found")
else:
    print("Not found")
