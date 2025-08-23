def solution(my_string, is_prefix):
    num = []
    for i in range(len(my_string)):
        num.append(my_string[0:i+1])
    return 1 if is_prefix in num else 0