import sys

input = sys.stdin.readline

n=int(input())
MOD=1000000007

def calc(n):
    if n==0:
        return (0,1)
    a,b=calc(n//2) #k, k+1
    c=(a*((2*b-a)%MOD))%MOD #2k=k(2k+1-k)
    d=(a*a+b*b)%MOD #2k+1
    if n%2==0:
        return (c,d) #2k, 2k+1
    else:
        return (d,(c+d)%MOD)

print(calc(n)[0])
