def solution(numLog):
    operation = {1: "w", -1: "s", 10: "d", -10: "a"}
    result = []

    for i in range(1, len(numLog)):
        diff = numLog[i] - numLog[i-1]
        if diff in operation:
            result.append(operation[diff])

    return "".join(result)


