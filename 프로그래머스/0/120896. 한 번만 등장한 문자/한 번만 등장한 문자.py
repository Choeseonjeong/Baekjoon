def solution(s):
    answer = ''
    words = set(s)
    for word in words:
        if s.count(word) == 1:
            answer+=word
    return ''.join(sorted(answer))