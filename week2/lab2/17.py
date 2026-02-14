n = int(input())

cnt = {}

for _ in range(n):
    phone = input().strip()
    cnt[phone] = cnt.get(phone, 0) + 1

ans = 0
for phone in cnt:
    if cnt[phone] == 3:
        ans += 1

print(ans)
