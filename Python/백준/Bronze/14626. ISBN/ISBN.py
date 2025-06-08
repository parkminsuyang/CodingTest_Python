import sys
import math

input=sys.stdin.readline
n=input().strip()
res=0
fores=0
for i in range(len(n)):
    if n[i]=='*':
        res=i
    else:
        if i%2==0:
            fores+=int(n[i])
        else:
            fores+=int(n[i])*3

for i in range(10):
    if res % 2 == 0:
        check = fores + i
    else:
        check = fores + i * 3
    if check % 10 == 0:
        print(i)
        break
