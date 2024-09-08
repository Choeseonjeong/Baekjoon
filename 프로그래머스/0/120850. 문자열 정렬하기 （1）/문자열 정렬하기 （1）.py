def solution(my_string):
    arr = ['1','2','3','4','5','6','7','8','9','0']
    answer =[]
    for i in list(my_string):
        if i in arr:
            answer.append(int(i))
    return sorted(answer)
