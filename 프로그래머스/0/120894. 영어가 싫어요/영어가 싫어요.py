def solution(numbers):
    word = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine" ]
    
    for i,n in enumerate(word):
        numbers = numbers.replace(n, str(i))
        
    answer = int(numbers)
    return answer