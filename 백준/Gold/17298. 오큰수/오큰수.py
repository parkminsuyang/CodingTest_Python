
import sys
n=int(sys.stdin.readline())
num=list(map(int,sys.stdin.readline().split()))
result=[-1]*n
stack=[]

for i in range(n):
    while stack and num[stack[-1]]<num[i]: #스택에 값이 있고, num[스택 젤 뒤]<num[i]면
        j=stack.pop() #j에 오큰수 짝 값 인덱스 할당
        result[j]=num[i] #결과값에 오큰수 할당

    stack.append(i) #스택에 오큰수 없는 값 추가

print(*result)



