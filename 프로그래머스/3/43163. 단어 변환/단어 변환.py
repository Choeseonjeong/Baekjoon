from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0

    L = len(begin)
    q = deque([(begin, 0)])
    visited = set([begin])

    while q:
        word, depth = q.popleft()
        if word == target:
            return depth

        for text in words:
            if text in visited:
                continue
            diff = sum(1 for i in range(L) if word[i] != text[i])
            if diff == 1:
                visited.add(text)
                q.append((text, depth + 1))

    return 0
