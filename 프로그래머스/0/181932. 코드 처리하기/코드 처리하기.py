def solution(code):
    ret = ''
    mode = 0
    for idx in range(len(code)):
        if code[idx] == '1' and mode == 0:
            mode = 1
            
        elif code[idx] == '1' and mode == 1:
            mode = 0
            
        if mode == 0 and idx%2==0 and code[idx] != '1':
            ret+=code[idx]
        elif mode == 1 and idx%2==1 and code[idx] != '1':
            ret+=code[idx]
        
    return ret if ret != '' else 'EMPTY'