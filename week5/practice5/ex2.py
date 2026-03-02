import re

s = input()
if re.fullmatch(r"ab{2,3}", s):
    print("Match")
else:
    print("No match")

#ab{2,3} → a және дәл 2 немесе 3 b.
