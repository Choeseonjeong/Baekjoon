def solution(my_string):
    answer = []
    return sorted([int(word) for word in my_string if word.isdigit()])