import sys
input=sys.stdin.readline

n,m=map(int,input().split())
dic=set()
cnt=0

class TrieNode:
    def __init__(self):
        self.children={}
        self.is_end=False

class Trie:
    def __init__(self):
        self.root=TrieNode()

    def insert(self,word):
        node=self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch]=TrieNode()
            node=node.children[ch]
            
        node.is_end=TrieNode
    
    def search(self,word):
        node=self.root
        for ch in word:
            if ch not in node.children:
                return False
            node=node.children[ch]
        return node.is_end

trie=Trie()
for _ in range(n):
    word=input().strip()
    trie.insert(word)

cnt=0
for _ in range(m):
    word=input().strip()
    if trie.search(word):
        cnt+=1
    
print(cnt)
