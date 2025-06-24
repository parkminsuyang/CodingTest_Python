import sys
input=sys.stdin.readline
a,b=map(int,input().split())

res=1
while True:
    tempb=int(b//2)

    if b%10==1:
        b=b//10

    elif b%2==0:
        b=tempb

    else:
        print(-1)
        break

    res += 1

    if a==b:
        print(res)
        break

    elif a>b:
        print(-1)
        break
