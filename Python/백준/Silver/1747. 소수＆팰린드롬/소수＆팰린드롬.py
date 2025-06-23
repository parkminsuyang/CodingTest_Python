import sys
input=sys.stdin.readline

def sosu(n):
    if n < 2:
        return False
    for i in range(2,int(n**1/2)+1):
        if n%i==0:
            return False
    else:
        return True
def pellin(n):
    nn=str(n)
    if nn[::-1]==nn:
        return True
    else:
        return False

n=int(input())
while True:
    if pellin(n) and sosu(n)==True:
        print(n)
        break
    else:
        n+=1