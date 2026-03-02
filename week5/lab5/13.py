import re
a=input()
b=re.findall(r"\w+", a)
print(len(b))