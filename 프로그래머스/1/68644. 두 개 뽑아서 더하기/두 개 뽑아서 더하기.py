from itertools import permutations
def solution(numbers):
    answer = set()
    for i in permutations(numbers,2):
        answer.add(sum(i))
    return sorted(list(answer))