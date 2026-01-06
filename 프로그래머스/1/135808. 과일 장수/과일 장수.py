import math
def solution(k, m, score):
    score = sorted(score)
    n = math.ceil(len(score)/m)
    while len(score) != n * m:
        score = [0] + score
    return sum([i*m for i in score[0::m]])