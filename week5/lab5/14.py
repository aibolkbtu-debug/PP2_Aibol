import re

pattern = re.compile(r"\d+")
text = input()

if pattern.fullmatch(text):
    print("Match")
else:
    print("No match")