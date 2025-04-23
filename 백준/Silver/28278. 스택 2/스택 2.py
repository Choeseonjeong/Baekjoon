import sys

n = int(input())
arr = []
for _ in range(n):
    command = sys.stdin.readline().split()
    if command[0] == '1':
        arr.append(command[1])
    elif command[0] == '2':
        if arr:
            print(arr.pop())
        else:
            print(-1)
    elif command[0] == '3':
        print(len(arr))
    elif command[0] == '4':
        if arr:
            print(0)
        else:
            print(1)
    elif command[0] == '5':
        if arr:
            print(arr[-1])
        else:
            print(-1)