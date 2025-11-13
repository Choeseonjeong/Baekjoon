def solution(my_string):
    word = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    arr = {}
    for n in word:
        arr[n] = 0
    for text in my_string:
        if text in arr:
            arr[text] += 1
    return [n for n in arr.values()]