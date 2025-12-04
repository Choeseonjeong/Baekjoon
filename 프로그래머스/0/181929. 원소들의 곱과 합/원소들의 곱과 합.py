def solution(num_list):
    answer = 1
    for i in num_list:
        answer*=i
    return 1 if answer < sum(i for i in num_list)*sum(i for i in num_list) else 0