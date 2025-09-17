def solution(c):
    c.sort(reverse = True)
    answer = 0
    for idx, book in enumerate(c):
        if book >= idx+1:
            h_index = idx+1
            answer = h_index
    return answer