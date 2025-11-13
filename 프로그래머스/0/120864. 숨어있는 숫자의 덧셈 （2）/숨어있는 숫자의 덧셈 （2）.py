def solution(my_string):
    answer = 'abcdefghijklmnopqrstuvwxyz'
    num = 0
    my_string = my_string.lower()
    for word in my_string:
        if word in answer:
            my_string = my_string.replace(word," ")
    for text in my_string.split(" "):
        if text != '':
            num += int(text)
    return num