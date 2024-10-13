n = int(input())
a = list(map(int, input().split()))

d = 0

for  i in range(n):
    d = d*10 + a[i]%10

if d%10 == 0:
    print("Yes")
else:
    print("No")