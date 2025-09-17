def solution(phone_book):
    answer = True
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    
    for phone_number in phone_book:
        word = ''
        for text in phone_number:
            word+=text
            if word in hash_map and word != phone_number:
                return False
    return answer