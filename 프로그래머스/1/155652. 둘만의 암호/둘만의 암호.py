def solution(s, skip, index):
    answer = 'abcdefghijklmnopqrstuvwxyz'
    result = ''
    for ch in list(skip):
        answer = answer.replace(ch,"")
            
    for a in s:
        result += answer[(answer.find(a) + index) % len(answer)]
    return result