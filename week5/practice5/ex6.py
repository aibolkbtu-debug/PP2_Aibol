import re

s = input()
result = re.sub(r"[ ,\.]", ":", s)
print(result)

#Бос орын, үтір, нүктені : таңбасына ауыстырады.