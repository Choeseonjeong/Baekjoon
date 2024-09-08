def solution(str1, str2):
    sum = ""
    for i in range(0, len(str1)):
        sum = sum + str1[i] + str2[i]
    return sum