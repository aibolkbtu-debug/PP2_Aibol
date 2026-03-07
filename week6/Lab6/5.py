s = input().lower()
m = "aeiou"

if any(x in m for x in s):
    print("Yes")
else:
    print("No")