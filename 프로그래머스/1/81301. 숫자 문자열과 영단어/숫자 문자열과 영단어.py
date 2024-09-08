def solution(s):
    dic = ["zero","one","two","three","four","five","six","seven","eight","nine"]
    
    for i in dic:
        if i in s:
            s = s.replace(i,str(dic.index(i)))
    return int(s)

