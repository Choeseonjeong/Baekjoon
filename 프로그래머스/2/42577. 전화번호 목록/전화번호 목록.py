def solution(phone_book):
    book = dict()
    for i in phone_book:
        book[i] = 1
    for num in phone_book:
        ch = ''
        for n in num:
            ch+=n
            if ch in book and ch!=num:
                
                return False
    return True