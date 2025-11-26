def solution(score):
    avg = [(a+b)/2 for a, b in score]
    rank = sorted(avg, reverse=True)
    return [rank.index(x) + 1 for x in avg]

