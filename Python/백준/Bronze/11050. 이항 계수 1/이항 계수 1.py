#자연수 n 정수 k
#이항계수 (n k)

n,k=map(int,input().split())
a=1
b=1
c=1
for i in range(1,n+1):
    a*=i

for j in range(1,k+1):
    b*=j

for f in range(1,n-k+1):
    c*=f
print(a//(b*c))
