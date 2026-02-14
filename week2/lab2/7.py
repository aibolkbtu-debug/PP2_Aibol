n = int(input())
a = list(map(int, input().split()))
max_val = a[0]
pos = 0
for i in range(n):
    if a[i] > max_val:
        max_val = a[i]
        pos = i
print(pos+1)