def solution(num_list):
    a = []
    b = []
    for i in num_list:
        if i % 2 == 0:
            a.append(str(i))
        else:
            b.append(str(i))

    a_str = "".join(a)
    b_str = "".join(b)
    return int(a_str) + int(b_str)
