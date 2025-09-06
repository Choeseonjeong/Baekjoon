def solution(elements):
    arr = elements*2
    lennum = len(elements)
    answer = set()
    for num in range(1,lennum+1):
        for i in range(num+lennum):
            answer.add(sum(arr[i:i+num]))
    return len(answer)