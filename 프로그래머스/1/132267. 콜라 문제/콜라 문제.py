def solution(a, b, n):
    answer = 0
    while n >= a:  
        new_colas = (n // a) * b  
        answer += new_colas  
        n = new_colas + (n % a)
    return answer   


# a만큼의 빈병가져가면 b만큼의 콜라 줌
# n개 가져다주면 몇 개 반환?
