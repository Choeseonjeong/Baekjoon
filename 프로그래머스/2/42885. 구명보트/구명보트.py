def solution(people, limit):
    ans = 0
    front = 0
    back = len(people)-1
    people.sort()
    
    while front < back:
        if people[front]+people[back]<=limit:
            ans += 1
            front += 1
        back -= 1
    return len(people)-ans
        