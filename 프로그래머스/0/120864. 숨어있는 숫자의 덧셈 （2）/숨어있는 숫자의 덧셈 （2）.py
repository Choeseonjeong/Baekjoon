def solution(my_string):
    my_string = list(my_string)
    answer = 0
    text = "0"
    for word in my_string:
        if word.isdigit():
            text+=word
        else:
            if text != "":
                answer += int(text)
                text = ""
    if text != "":
        answer += int(text)
    return answer