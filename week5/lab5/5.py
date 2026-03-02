import re

s = input()

pattern = r'^[A-Za-z].*\d$'

if re.search(pattern, s):
    print("Yes")
else:
    print("No")