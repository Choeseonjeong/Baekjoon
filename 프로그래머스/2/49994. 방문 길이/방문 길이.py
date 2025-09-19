def solution(dirs):
    walk = {"U":(0,1),"D":(0,-1),"R":(1,0),"L":(-1,0)}
    x,y = 0,0
    
    load = set()
    x,y = 0,0
    for text in dirs:
        dx,dy = walk[text]
        nx,ny = x+dx,y+dy
        if abs(nx) <= 5 and abs(ny) <= 5:
            edge = tuple(sorted([(x, y), (nx, ny)]))
            load.add(edge)
            x,y = nx,ny
    return len(load)
            