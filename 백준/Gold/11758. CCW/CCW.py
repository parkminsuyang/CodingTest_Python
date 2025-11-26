import sys

input=sys.stdin.readline
p1=(tuple(map(int,input().split())))
p2=(tuple(map(int,input().split())))
p3=(tuple(map(int,input().split())))

#val=(x2-x1)(y3-y1)+(y2-y1)(x3-x1)
val=(p2[0]-p1[0])*(p3[1]-p1[1])-(p2[1]-p1[1])*(p3[0]-p1[0])
if val>0:
    print(1)
elif val<0:
    print(-1)
else:
    print(0)