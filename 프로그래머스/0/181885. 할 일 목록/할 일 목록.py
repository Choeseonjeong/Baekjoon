def solution(todo_list, finished):
    answer = [todo for todo,flag in zip(todo_list, finished) if flag==False]
    return answer