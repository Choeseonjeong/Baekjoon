def solution(dots):
    x = [a for a,b in dots]
    y = [b for a,b in dots]
    
    w = max(x)-min(x)
    h = max(y)-min(y)
    
    return w*h