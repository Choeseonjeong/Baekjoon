def solution(phone_book):
    arr = {}
    answer = {}
    for i in phone_book:
        arr[i]=1
    for num in phone_book:
        ch = ''
        for j in num:
            ch+=j
            if ch in arr and ch!= num:
                return False
    return True 