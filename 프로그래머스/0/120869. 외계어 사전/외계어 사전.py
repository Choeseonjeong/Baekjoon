import itertools
def solution(spell, dic):
    arr = [''.join(p) for p in itertools.permutations(spell, len(spell))]
    for word in arr:
        if word in dic:
            return 1
    return 2