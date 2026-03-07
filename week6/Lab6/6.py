n = int(input())
m = map(int, input().split())
if all(x>=0 for x in m):
    print("Yes")
else:
    print("No")