n = int(input())
a = list(map(int, input().split()))
sum = 0
for x in a:
    if x >0:
        sum+=1
print(sum)