def solution(my_strings, parts):
    answer = ''
    result = ''
    for i in range(len(parts)):
        x,y = parts[i][0],parts[i][1]
        answer+=my_strings[i][x:y+1]
    return answer