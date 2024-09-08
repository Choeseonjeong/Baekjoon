# 기능개발
import math
from collections import deque


def solution(progresses, speeds):
    a = []
    stack = []
    front = 0
    for i in range(len(progresses)):
        b = (100 - progresses[i]) / speeds[i]
        a.append(math.ceil(b))

    for i in range(len(a)):
        if a[i] > a[front]:
            stack.append(i - front)
            front = i
    stack.append(len(a) - front)

    return stack