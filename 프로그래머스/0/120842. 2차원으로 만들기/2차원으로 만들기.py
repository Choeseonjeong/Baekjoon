def solution(num_list, n):
    answer = []
    num = 0
    for _ in range(len(num_list)//n):
        answer.append(num_list[num:n+num])
        num = num+n
    return answer