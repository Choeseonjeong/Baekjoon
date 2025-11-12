def solution(numbers):
    arr = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for idx, word in enumerate(arr):
        numbers = numbers.replace(word, str(idx))
    return int(numbers)