def solution(arr):
    stk = []
    for num in arr:
        if len(stk)==0:
            stk.append(num)
        elif stk[-1] == num:
            stk.pop()
        elif stk[-1] != num:
            stk.append(num)
    return stk if len(stk) != 0 else [-1]
        

# 빈 배열이면 arr[i] 추가
# 마지막 원소가 같으면 마지막 원소 제거
# 다르면 추가 