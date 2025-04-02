def solution(age):
    answer = ''
    proAge = {chr(i): i - ord('a') for i in range(ord('a'), ord('j') + 1)}
    reversedProAge = {v: k for k, v in proAge.items()}
    for i in list(str(age)):
        answer+=str(reversedProAge[int(i)])
    return answer