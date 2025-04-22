arrs = [1,1,2,2,2,8]
nums = list(map(int, input().split()))
result = ''
for i in range(len(arrs)):
    result+=str((arrs[i]-nums[i]))+" "
print(result)
