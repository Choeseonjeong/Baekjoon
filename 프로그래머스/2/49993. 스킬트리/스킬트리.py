def solution(skill, skill_trees):
    arr = 0
    for tree in skill_trees:
        ch = ''
        for n in tree:
            if n in skill:
                ch+=n
        if skill[:len(ch)]==ch:
            arr+=1
    return arr