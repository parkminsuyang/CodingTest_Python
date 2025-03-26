a,b,v=map(int,input().split())
day=0
if v%(a-b)==0:
    day=(v//(a-b))-1
else:
    day = (v // (a - b))
if (v-a)//(a-b)<=day:
    if((v-a)%(a-b)==0):
        print((v-a)//(a-b)+1)
    else:
        print((v - a) // (a - b) + 2)
else:
    print(day)
