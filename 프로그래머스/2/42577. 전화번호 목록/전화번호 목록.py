def solution(phone_book):
    dic = dict()
    for nums in phone_book:
        dic[nums] = 1
        
    for nums in phone_book:
        word = ''
        for num in nums:
            word+=num
            if word in dic and word!= nums:
                return False
    return True