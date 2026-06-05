def solution(s):
    change_count = 0 
    zero_count = 0   
    
    while s != '1':
        zero_count += s.count('0')
        s = s.replace('0', '')
        current_len = len(s)
        s = bin(current_len)[2:]
        change_count += 1
    return [change_count, zero_count]