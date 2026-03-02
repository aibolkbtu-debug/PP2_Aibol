import re
text = input()
result = re.match("Hello", text)
if result:
    print("Yes")
else:
    print("No")