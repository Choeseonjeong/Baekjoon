from itertools import permutations
def solution(spell, dic):
    arr = []
    for i in permutations(spell,len(spell)):
        word = ''.join(i)
        if word in dic:
            return 1
    return 2