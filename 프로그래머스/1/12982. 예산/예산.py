def solution(d, budget):
    d.sort()  # 작은 금액부터 처리하기 위해 정렬
    total = 0  # 사용한 예산 합
    cnt = 0  # 지원 가능한 부서 수
    
    for cost in d:
        if total + cost > budget:  # 예산 초과 시 중단
            break
        total += cost
        cnt += 1  # 부서 개수 증가

    return cnt
