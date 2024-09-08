def solution(my_string):
    answer = ''
    for i in list(my_string):
        if i.isupper():
            answer+=i.lower()
        else:
            answer+=i.upper()
    return answer