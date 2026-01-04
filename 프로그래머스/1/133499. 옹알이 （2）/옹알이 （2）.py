def solution(babbling):
    word = ["aya", "ye", "woo", "ma"]
    answer = []
    for bab in babbling:
        for i in word:
            if i * 2 not in bab:  
                bab = bab.replace(i, ' ')
        answer.append(list(set(bab)))
    return answer.count([" "])