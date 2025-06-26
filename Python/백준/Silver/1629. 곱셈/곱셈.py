import sys
input=sys.stdin.readline

a,b,c=map(int,input().split())

a=a%c
res=1
while b>0:
    if b%2==1:
        res=(res*a)%c
    a=(a*a)%c
    b//=2
print(res)