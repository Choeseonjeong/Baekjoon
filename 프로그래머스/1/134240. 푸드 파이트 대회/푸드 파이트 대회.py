def solution(food):
    arr=[]
    answer=[]
    for i in food:
        a = i//2
        arr.append(a)
    for i in range(len(arr)):
        for j in range(arr[i]):
            answer.append(i)
    return "".join(map(str,answer))+str(0)+"".join(map(str,answer[::-1])) 