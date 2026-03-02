import re

s = input()
if re.fullmatch(r"ab*", s):
    print("Match")
else:
    print("No match")

#ab* → a әрпінен басталып, кейін 0 немесе одан көп b келеді.
