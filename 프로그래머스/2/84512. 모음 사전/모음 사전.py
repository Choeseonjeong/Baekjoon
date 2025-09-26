from itertools import product
def solution(word):
    text = ['A', 'E', 'I', 'O', 'U']
    all = []
    for i in range(1,len(text)+1):
        for j in product(text,repeat = i):
            all.append(''.join(j))
    return sorted(all).index(word)+1