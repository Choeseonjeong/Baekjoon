from collections import Counter
def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    
    arr1 = [str1[i:i+2] for i in range(len(str1)-1) if str1[i:i+2].isalpha()]
    arr2 = [str2[i:i+2] for i in range(len(str2)-1)if str2[i:i+2].isalpha()]
    
    c1 = Counter(arr1)
    c2 = Counter(arr2)
    
    ans1 = list((c1&c2).elements())
    ans2 = list((c1|c2).elements())
    
    if len(ans2) == 0:
        return 65536
    
    return int((len(ans1)/len(ans2))*65536)