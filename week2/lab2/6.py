n = int(input())
a = list(map(int, input().split()))
s = -999999999999
for x in a:
    if x >s:
        s=x
print(s)