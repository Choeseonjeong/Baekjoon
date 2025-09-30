def solution(s):
    answer = [int(i) for i in s.split(" ")]
    return ' '.join((str(min(answer)),str(max(answer))))