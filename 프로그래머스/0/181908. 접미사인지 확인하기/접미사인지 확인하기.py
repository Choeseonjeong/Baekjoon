def solution(my_string, is_suffix):
    answer = 0
    ch = ''
    for idx,ch in enumerate(my_string):
        if is_suffix == my_string[idx:]:
            return 1
    return 0