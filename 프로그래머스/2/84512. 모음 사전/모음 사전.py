from itertools import product

def solution(word):
    words = ['A','E','I','O','U']
    allP = []
    for i in range(len(words)):
        for j in product(words, repeat=i+1):
             allP.append(''.join(j))
    allP.sort()
    return allP.index(word)+1