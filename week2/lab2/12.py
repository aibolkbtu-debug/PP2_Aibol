n = int(input())
a = list(map(int, input().split()))
new=[]
for x in a:
    x**=2
    new.append(x)
print(*new)