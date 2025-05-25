import sys
from os import remove

input=sys.stdin.readline
m=int(input())
s=[]

for _ in range(m):
    a=input().split()
    if a[0]=='add':
        if int(a[1]) in s:
            pass
        else:
            s.append(int(a[1]))
    elif a[0]=='remove':
        if int(a[1]) in s:
            s.remove(int(a[1]))
        else:
            pass
    elif a[0]=='check':
        if int(a[1]) in s:
            print(1)
        else:
            print(0)
    elif a[0]=='toggle':
        if int(a[1]) in s:
            s.remove(int(a[1]))
        else:
            s.append(int(a[1]))

    elif a[0]=='all':
        s=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    elif a[0]=='empty':
        s=[]
