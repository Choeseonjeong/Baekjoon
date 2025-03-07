def solution(my_string, is_suffix):
    arr = []
    for i in range(len(my_string)):
        arr.append(my_string[i:])
    return int(is_suffix in arr)