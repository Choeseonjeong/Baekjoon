def solution(arr):
    answer = []
    row = len(arr)
    col = len(arr[0])
    if row > col: 
        for ilist in arr:
            ilist.extend([0]*(row-col))
        return arr
    elif row < col:
        for _ in range(col-row):
            arr.append([0]*col)
        return arr
    else:
        return arr