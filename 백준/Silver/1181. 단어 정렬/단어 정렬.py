n=int(input())
words=[]
for i in range(n):
    words.append(input())
words=list(set(words))
words.sort()
words.sort(key=len)


for w in words:
    print(w)