def solution(phone_book):
    hash_map = dict()
    for num in phone_book:
        hash_map[num] = 1
        
    for number in hash_map:
        ch = ''
        for n in number:
            ch+=n
            if ch in hash_map and ch!=number:
                return False
    return True