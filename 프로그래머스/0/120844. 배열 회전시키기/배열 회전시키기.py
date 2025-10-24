def solution(numbers, direction):
    answer = []
    if direction == "left":
        return numbers[1:]+[numbers[0]]
    else:
        return [numbers[-1]]+numbers[:len(numbers)-1]