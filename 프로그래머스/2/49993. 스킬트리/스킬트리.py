def solution(skill, skill_trees):
    words = []
    flag = [True]*len(skill_trees)
    answer = 0
    for tree in skill_trees:
        ch = ''
        for text in tree:
            if text in skill:
                ch+=text
        words.append(ch)
        
    for idx, word in enumerate(words):
        for i in range(len(word)):
            if word[i] != skill[i]:
                flag[idx]=False
    return flag.count(True)
                
        