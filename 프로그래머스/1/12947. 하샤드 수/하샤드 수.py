def solution(x):
    answer = sum([int(n) for n in str(x)])
    return True if x%answer == 0 else False