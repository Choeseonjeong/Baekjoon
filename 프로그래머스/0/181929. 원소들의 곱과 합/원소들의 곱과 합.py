def solution(num_list):
    ans1 = 1
    ans2 = 0
    for num in num_list:
        ans1*=num
        ans2 += num
    ans2 = ans2*ans2
    return 1 if ans1<ans2 else 0