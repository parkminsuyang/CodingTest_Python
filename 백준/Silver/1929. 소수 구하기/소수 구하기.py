import sys

input=sys.stdin.readline
n,m=map(int,input().split())

for i in range(n,m+1):
    if i==1:
        continue
    else:
        for j in range(2,int(i**(1/2))+1):
            if i%j==0:
                break
        else:
            print(i)
