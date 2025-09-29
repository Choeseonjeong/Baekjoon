def solution(myString, pat):
    answer = 0
    myString = myString.replace("A","C").replace("B","A").replace("C","B")
    return 1 if pat in myString else 0