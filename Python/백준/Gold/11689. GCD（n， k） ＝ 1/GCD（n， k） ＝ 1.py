import sys
input=sys.stdin.readline
n=int(input())
result=n
i=2
while i*i<=n:
    if n%i==0:
        while n%i==0:
            n//=i
        result-=result//i
    i+=1
if n>1:
    result-=result//n
print(result)
