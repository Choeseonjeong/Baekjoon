def solution(skill, skill_trees):
    arr = []
    count = 0
    for s in skill_trees:
        ch = ''
        for i in s:
            if i in skill:
                ch+=i
        if skill[:len(ch)] == ch:     
            count += 1
    return count
    