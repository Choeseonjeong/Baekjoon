def solution(arr):
    count = 0
    prev = arr.copy()
    while True:
        new_arr = []
        for x in prev:
            if x >= 50 and x % 2 == 0:
                new_arr.append(x // 2)
            elif x < 50 and x % 2 == 1:
                new_arr.append(x * 2 + 1)
            else:
                new_arr.append(x)
        
        if new_arr == prev:  
            break
        prev = new_arr
        count += 1
    
    return count
