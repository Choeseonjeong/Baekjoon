num_people, cut_people = map(int, input().split(" "))
arr = list(map(int,input().split(" ")))
arr = sorted(arr, reverse=True)
print(arr[cut_people-1])