def solution(s):
    word = {}
    answer = [-1]*len(s)
    for idx, ch in enumerate(s):
        if ch not in word:
            word[ch] = idx
        else:
            answer[idx] = idx - word[ch]
            word[ch] = idx
    return answer