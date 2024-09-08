def solution(numbers):
    numbers.sort()
    return (
        int(numbers[-1]) * int(numbers[-2])
        if int(numbers[-1]) * int(numbers[-2]) > int(numbers[0]) * int(numbers[1])
        else int(numbers[0]) * int(numbers[1])
    )