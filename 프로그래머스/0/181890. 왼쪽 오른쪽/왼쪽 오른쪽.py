# 먼저 나오는 l or r
# l : 왼쪽 담기
# r : 오른쪽 담기 
def solution(str_list):
    for idx, val in enumerate(str_list):
        if val=="l":
            return str_list[:idx]
        if val=="r":
            return str_list[idx+1:]
    return []