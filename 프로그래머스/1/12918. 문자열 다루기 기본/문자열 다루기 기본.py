def solution(s):
    if len(s) == 4 or len(s) == 6:
        for i in s:
            if i < "0" or i > "9":
                return False
        return True
    else:
        return False
