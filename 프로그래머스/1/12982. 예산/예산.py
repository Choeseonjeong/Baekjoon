def solution(d, budget):
    num = sorted(d)  # 요청 금액을 오름차순으로 정렬
    arr = 0  # 현재까지 사용된 예산
    result = 0  # 지원 가능한 부서의 수
    for i in num:
        if i+arr>budget:
            break
        arr+=i
        result+=1
    return result