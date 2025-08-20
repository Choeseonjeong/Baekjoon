def solution(todo_list, finished):
    result = []
    for key, value in zip(todo_list, finished):
        if value == False:
            result.append(key)
    return result