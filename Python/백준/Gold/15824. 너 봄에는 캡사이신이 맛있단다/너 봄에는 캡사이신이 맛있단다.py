import sys
input=sys.stdin.readline

n=int(input())
spicy=list(map(int,input().split()))
spicy.sort()
res=0
length=len(spicy)
MOD = 1_000_000_007

pow2 = [1] * (length+1)
for i in range(1, length+1):
    pow2[i] = (pow2[i-1] * 2) % MOD

for i in range(length):
    res-=spicy[i]*(pow2[length-i-1])
    res+=spicy[i]*(pow2[i])
    res%=MOD
print(res)