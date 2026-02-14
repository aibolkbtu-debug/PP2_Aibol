n = int(input())
a = list(map(int, input().split()))
new=[]
for i in a:
    if i in new:
        print("NO")
    else:
        new.append(i)
        print("YES")