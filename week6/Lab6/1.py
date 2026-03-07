n=int(input())
m=map(int, input().split())
s = 0
for x in m:
    s+=x**2
print(s)