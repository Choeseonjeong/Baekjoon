def solution(chicken):
    coupon = chicken
    answer = 0
    while coupon >= 10:
        service = coupon//10
        answer += service
        coupon = service + coupon%10
    return answer