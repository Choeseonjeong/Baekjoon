def solution(s, n):
    a = 'abcdefghijklmnopqrstuvwxyz'
    b = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    answer = ''
    for ch in list(s):
        if ch.isupper():
            answer += b[(b.find(ch)+n)%len(b)]
        elif ch.islower():
            answer += a[(a.find(ch)+n)%len(a)]
        elif ch == ' ':
            answer += ' '
    return answer