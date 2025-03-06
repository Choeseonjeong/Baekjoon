def solution(todo_list, finished):
    arr = dict(zip(todo_list,finished))
    result = []
    for key, values in arr.items():
        if values==False:
            result.append(key)
    return result