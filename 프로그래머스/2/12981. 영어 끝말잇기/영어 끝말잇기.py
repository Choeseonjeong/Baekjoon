def solution(n, words):
    stack = [words[0]]
    result = [0,0]
    for i in range(1,len(words)):
        if stack[-1][-1] != words[i][0] or words[i] in stack:
            return [i%n+1,i//n+1]
        else:
            stack.append(words[i])
    return result