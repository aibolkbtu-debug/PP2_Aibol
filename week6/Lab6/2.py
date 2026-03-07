n=int(input())
m=map(int, input().split())
n=list(filter(lambda x: x%2==0, m))
s=0
for i in n:
    s+=1
print(s)