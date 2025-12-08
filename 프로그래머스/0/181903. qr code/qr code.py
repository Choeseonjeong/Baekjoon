def solution(q, r, code):
    answer = ''
    for idx, word in enumerate(code):
        if idx%q==r:
            answer+=word
    return answer