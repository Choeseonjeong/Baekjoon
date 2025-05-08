import sys
input = sys.stdin.readline

N,M = map(int,input().split())
memo = dict()
for _ in range(N):
    text = input().rstrip()
    if len(text) < M:
        continue         
    if text not in memo:       
        memo[text] = 0        
    memo[text] += 1    
    
result = sorted(memo.items(), key=lambda kv: (-kv[1],-len(kv[0]),kv[0]))
for word, _ in result:
    print(word)