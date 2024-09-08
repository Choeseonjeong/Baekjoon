n, k = map(int, input().split(" "))
count = 0
a = []
for i in range(n):
    num = int(input())
    a.append(num)

a.sort(reverse=True)  # 내림차순 정렬

for coin in a:
    if k >= coin:  # 동전의 가치가 k보다 작거나 같을 때만 사용 가능
        count += k // coin  # 해당 동전으로 몇 개를 사용할 수 있는지 계산
        k %= coin  # 남은 금액 갱신

print(count)
