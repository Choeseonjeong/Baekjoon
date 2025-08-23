# 존재한다면 2 ㄴㄴ면 2
def solution(spell, dic):
    spell = set(spell)
    for word in dic:
        if not spell - set(word):
            return 1
    return 2