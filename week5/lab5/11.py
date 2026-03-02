import re
text = input()
numbers = re.findall("[A-Z]", text)
print(len(numbers))