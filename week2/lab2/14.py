n = int(input())
a = list(map(int, input().split()))
cnt = {}
for x in a:
    if x in cnt:
        cnt[x] += 1
    else:
        cnt[x] = 1
mx = max(cnt.values())
ans = None
for x in cnt:
    if cnt[x] == mx:
        if ans is None or x < ans:
            ans = x
print(ans)
