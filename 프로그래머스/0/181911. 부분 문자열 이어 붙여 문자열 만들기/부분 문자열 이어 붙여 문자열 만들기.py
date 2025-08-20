def solution(my_strings, parts):
    answer = ''
    for i in range(len(my_strings)):
        x,y = parts[i]
        word = my_strings[i]
        answer+=word[x:y+1]
    return answer