def solution(s):
    answer = ''
    arr =[int(i) for i in s.split()]
    return str(min(arr))+ " " + str(max(arr))