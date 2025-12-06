def solution(my_string):
    answer = []
    for word in my_string:
        if word.isalpha():
            my_string = my_string.replace(word," ")
    my_string = my_string.split()
    return sum(list(map(int, my_string)))