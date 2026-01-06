def solution(number, limit, power):
    def nums(n):
        count = 0
        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                count += 2
        if int(n**0.5) ** 2 == n:
            count -= 1
        return count 
    
    num = []
    for j in range(1,number+1):
        a = nums(j)
        if a > limit:
            num.append(power)
        else:
            num.append(a)
    return sum(num)