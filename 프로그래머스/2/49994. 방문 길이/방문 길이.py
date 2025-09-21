def solution(dirs):
    nums = {"U":(1,0),"D":(-1,0),"R":(0,1),"L":(0,-1)}
    walks = set()
    x,y = 0,0
    for i in dirs:
        dx,dy = nums[i]
        nx,ny = x+dx,y+dy
        if abs(nx)<=5 and abs(ny)<=5:
            walks.add(((x,y),(nx,ny)))
            walks.add(((nx,ny),(x,y)))
            x, y = nx, ny
    return len(set(walks))//2
        
        