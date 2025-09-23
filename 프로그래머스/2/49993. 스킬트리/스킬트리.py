def solution(skill, skill_trees):
    count = 0
    arr = []
    for word in skill_trees:
        ch = ''
        for i in word:
            if i in skill:
                ch+=i
        if skill[:len(ch)]==ch:
            count+=1
    return count