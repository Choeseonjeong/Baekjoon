def solution(s):
    result = []
    for word in s.split(" "):
        answer = ''
        for idx in range(len(word)):
            if idx%2==0:
                answer += word[idx].upper()
            else:
                answer += word[idx].lower()
        result.append(answer)
    return ' '.join(result)
