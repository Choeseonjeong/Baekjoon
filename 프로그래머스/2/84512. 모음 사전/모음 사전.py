from itertools import product

def solution(word):
    text = ['A', 'E', 'I', 'O', 'U']
    all = set()
    for i in range(1,len(text)+1):
        for j in product(text,repeat=i):
            ch =''.join(j)
            all.add(ch)
    return sorted(list(all)).index(word)+1