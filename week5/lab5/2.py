import re
text = input()
find=input()
result = re.search(find, text)
if result:
    print("Yes")
else:
    print("No")