#ccw알고리즘
import sys

input=sys.stdin.readline

ax1,ay1,ax2,ay2=map(int,input().split())
bx1,by1,bx2,by2=map(int,input().split())

def ccw(Ax, Ay, Bx, By, Cx, Cy):
    return (Bx-Ax)*(Cy-Ay)-(Cx-Ax)*(By-Ay)

ccw1=ccw(ax1,ay1,ax2,ay2,bx1,by1)
ccw2=ccw(ax1,ay1,ax2,ay2,bx2,by2)
ccw3=ccw(bx1,by1,bx2,by2,ax1,ay1)
ccw4=ccw(bx1,by1,bx2,by2,ax2,ay2)

def on(x1,y1,x2,y2,x3,y3):
    return min(x1,x2)<=x3<=max(x1,x2) and min(y1,y2)<=y3<=max(y1,y2)
if (ccw1*ccw2)<0 and (ccw3*ccw4)<0:
    print(1)
elif ccw1==0 and on(ax1,ay1,ax2,ay2,bx1,by1):
    print(1)
elif ccw2==0 and on(ax1,ay1,ax2,ay2,bx2,by2):
    print(1)
elif ccw3==0 and on(bx1,by1,bx2,by2,ax1,ay1):
    print(1)
elif ccw4==0 and on(bx1,by1,bx2,by2,ax2,ay2):
    print(1)
else:
    print(0)