def solution(my_string, is_prefix):
    answer = []
    for idx, ch in enumerate(my_string):
        if my_string[0:len(my_string)-idx] == is_prefix:
            return 1
    return 0