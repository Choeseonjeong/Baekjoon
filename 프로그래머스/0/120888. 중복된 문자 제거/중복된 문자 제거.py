def solution(my_string):
    ans = ''
    result = ''
    for i in my_string:
        if i not in ans:
            ans+=i
            result+=i
    return result