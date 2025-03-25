def solution(before, after):
    before = sorted(list(before))
    after = sorted(list(after))
    for i in range(len(before)):
        if before[i]==after[i]:
            continue
        else:
            return 0
    return 1