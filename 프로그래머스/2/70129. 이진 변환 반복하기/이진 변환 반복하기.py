def solution(s):
    result = 0  # 이진변환 수
    CountResult = 0  # 누적 0의 개수
    while s != "1":
        CountResult += s.count("0")
        s = bin(len(s) - s.count("0"))[2:]  # 길이-갯수 즉, 0을 제외한 수의 2진수
        result += 1
        if s == 1:
            break
    return result, CountResult