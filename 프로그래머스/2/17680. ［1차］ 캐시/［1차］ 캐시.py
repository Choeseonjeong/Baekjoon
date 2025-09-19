def solution(cacheSize, cities):
    cities = [i.lower() for i in cities]
    answer = {}
    time = 0
    if cacheSize == 0:
        return 5 * len(cities)
    
    for city in cities:
        # 모두 1 추가
        for k in list(answer.keys()):
            answer[k] += 1
        # 이미 존재하는건 0으로 초기화
        if city in answer:
            answer[city] = 0
            time += 1
        else: # 없으면 5 추가, 넣기, 삭제하기
            time += 5
            if len(answer) == cacheSize:
                mmax = max(answer,key=answer.get)
                del answer[mmax]
            answer[city] = 0
    return time