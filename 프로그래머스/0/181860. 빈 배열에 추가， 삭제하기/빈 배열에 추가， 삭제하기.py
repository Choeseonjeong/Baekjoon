def solution(arr, flag):
    result = []
    for key, value in zip(arr, flag):
        if value == True :
            result.extend([key] * (key*2))
        else:
            del result[-key:]
    return result