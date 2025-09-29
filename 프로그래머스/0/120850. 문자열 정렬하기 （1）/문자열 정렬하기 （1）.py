def solution(my_string):
    ans = []
    for i in my_string:
        if not i.isalpha():
            ans.append(int(i))
    return sorted(ans)
    
    