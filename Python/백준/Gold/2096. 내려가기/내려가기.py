import sys
input=sys.stdin.readline

n=int(input())
num=[]

for i in range(n):
    a,b,c=map(int,input().split())
    if i==0:
        min0,min1,min2=a,b,c
        max0,max1,max2=a,b,c
        continue
    min0,min1,min2=(min(min0,min1)+a),(min(min0, min1,min2)+b),(min(min1, min2)+c)
    max0, max1, max2 = (max(max0, max1) + a), (max(max0, max1, max2) + b), (max(max1, max2) + c)
print(max(max0,max1,max2),min(min0,min1,min2))