def solution(people, limit):
    people.sort()
    front, back = 0,len(people)-1
    count = 0
    while front <= back:
        if people[front] + people[back] > limit:
            back -= 1
            count += 1
        else:
            front+=1
            back-=1
            count+=1
    return count