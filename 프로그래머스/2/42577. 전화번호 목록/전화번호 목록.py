from collections import Counter

def solution(phone_book):
    hash_map = Counter(phone_book)
    
    for words in phone_book:
        ch = ''
        for word in words:
            ch += word
            if ch in hash_map and ch != words:
                return False
    return True