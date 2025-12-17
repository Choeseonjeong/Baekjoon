def solution(arr):
    stk = []
    for i in range(len(arr)):
        if not stk:
            stk.append(arr[i])
            i+=1
        elif len(stk)>0 and stk[-1]==arr[i]:
            del stk[-1:]
            i+=1
        elif len(stk) > 0 and stk[-1]!=arr[i]:
            stk.append(arr[i])
            i+=1
    return stk if stk else [-1]