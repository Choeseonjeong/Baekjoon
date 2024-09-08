def solution(hp):
    num=0
    num += hp//5
    hp = hp%5
    num += hp//3
    hp = hp%3
    num += hp//1
    hp = hp%1
    return num