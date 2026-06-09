def solution(numbers):
    result = [-1]*len(numbers)
    stack = []
    for idx, num in enumerate(numbers):
        while stack and numbers[stack[-1]] < num:
            result[stack.pop()] = num
        stack.append(idx)
    return result