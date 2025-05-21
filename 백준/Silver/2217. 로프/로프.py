import sys

input=sys.stdin.readline
loop=[]
n=int(input())
for i in range(n):
    loop.append(int(input()))



loop.sort(reverse=True)


div=loop[0]

if n>0:
    for i in range(1,n):


        if (i+1)*loop[i]>div:
            div=(i+1)*loop[i]


print(div)