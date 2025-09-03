def solution(people, limit):
    boat = 0
    people.sort()
    
    front,back = 0,len(people)-1
    while front < back:
        if people[front]+people[back] <= limit:
            front+=1
            boat+=1
        back-=1
    return len(people)-boat

        