import re
text = input()
find=input()
numbers = re.findall(find, text)

print(len(numbers))