def solution(num_list):
    ch = ''
    nh = ''
    for num in num_list:
        if num%2!=0:
            ch+=str(num)
        else:
            nh+=str(num)
    return int(ch)+int(nh)