def solution(arr, queries):
    answer = []
    for i in queries:
        i,j = i
        temp = arr[i]
        arr[i]=arr[j]
        arr[j]=temp
    return arr