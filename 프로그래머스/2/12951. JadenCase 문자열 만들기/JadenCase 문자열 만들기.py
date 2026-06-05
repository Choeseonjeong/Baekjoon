def solution(s):
    answer = ''
    for ch in s.split(' '):
        answer+=ch.capitalize()
        answer+=' '
    return answer[:-1]