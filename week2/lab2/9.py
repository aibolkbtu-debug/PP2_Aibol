n = int(input())
a = list(map(int, input().split()))
min_val = a[0]
max_val = a[0]
for x in a:
    if x < min_val:
        min_val = x
    if x > max_val:
        max_val = x
for i in range(n):
    if a[i] == max_val:
        a[i] = min_val
print(*a)
