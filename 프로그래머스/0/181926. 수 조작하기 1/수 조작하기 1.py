
def solution(n, control):
    control_list = list(control)
    result = n
    for i in control_list:
        if i == "w":
            result += 1
        elif i == "s":
            result -= 1
        elif i == "d":
            result += 10
        else:
            result -= 10
    return result
