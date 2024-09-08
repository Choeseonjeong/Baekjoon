
def solution(arr1, arr2):
    if len(arr1) == len(arr2):
        if sum(i for i in arr1) > sum(i for i in arr2):
            return 1
        elif sum(i for i in arr1) == sum(i for i in arr2):
            return 0
        else:
            return -1
    elif len(arr1) > len(arr2):
        return 1
    else:
        return -1
