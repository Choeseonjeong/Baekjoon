from itertools import product

def solution(word):
    words = ['A', 'E', 'I', 'O', 'U']
    all = []
    for i in range(1,6):
        for j in product(words,repeat=i):
            all.append(''.join(j))
    all.sort()
    return all.index(word)+1