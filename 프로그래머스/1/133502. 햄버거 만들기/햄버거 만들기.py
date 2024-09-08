def solution(ingredient):
    result = 0
    arr = []
    for i in ingredient:
        arr.append(i)
        if arr[-4:]==[1,2,3,1]:
            result+=1
            for _ in range(4):
                arr.pop()
    return result