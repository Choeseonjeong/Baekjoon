def solution(people, limit):
    people.sort()
    front,end = 0,len(people)-1
    answer = 0
    
    while front <= end:
        if people[front] + people[end] <= limit:
            answer += 1
            front += 1
            end -= 1
        else:
            end -=1
            answer += 1
    return answer