arr = []
while (a := int(input())) != -1:
    arr.append(a)
    
def solution(n):
    nums = []
    for num in range(1,n+1):
        if n % num == 0:
            nums.append(num)
    if sum(nums)-n==n:
        print(n,"=",end=' ')
        for i in range(len(nums)):
            if nums[i]==nums[-1]:
                print()
            elif nums[i]==nums[-2]:
                print(nums[i],end=" ")
            else:
                print(nums[i],"+",end=" ")
    else:
        print(n,"is NOT perfect.")
for j in arr:
    solution(j)
