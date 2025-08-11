import sys
from math import comb

input=sys.stdin.readline
n=int(input())
MOD=10007
ans=0
for i in range(1,n//4+1):
    val=(comb(13,i)%MOD)*(comb(52-(4*i),n-(4*i))%MOD)
    if i%2:
        ans+=val
    else:
        ans-=val
print(ans%MOD)