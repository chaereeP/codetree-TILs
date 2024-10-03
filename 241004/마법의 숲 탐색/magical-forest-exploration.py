# input
r, c, k = map(int, input().split())
arr = list()
for _ in range(k):
    arr.append(list(map(int, input().split())))

import queue
dx= [0, 1, 0, -1]
dy= [-1, 0, 1, 0]
A = [[0]*(c) for _ in range(r+3)]
exit_map = [[0]*(c) for _ in range(r+3)]

def occupied(x,y):
    if not A[y][x]:
            return False
    return True

def down(x, y):
    if occupied(x-1,y+1) or occupied(x, y+2) or occupied(x+1,y+1):
        return False
    return True
def left(x,y):
    if occupied(x-2,y) or occupied(x-1, y+1) or occupied(x-1,y-1):
        return False
    return True
def right(x,y):
    if occupied(x+2,y) or occupied(x+1, y+1) or occupied(x+1,y-1):
        return False
    return True
def inRange(x,y):
    if 0<=x<c and 3<=y<r+3:
        return True
    else: False
from collections import deque
def score_cal(x,y): # bfs
    max_y = y
    visited_arr =[[False]*(c) for _ in range(r+3)]
    q = deque([(x,y)])
    visited_arr[y][x] = True
    while q:
        now_x, now_y = q.popleft()
        for j in range(4):
            nx, ny = now_x+dx[j], now_y+dy[j]
            if inRange(nx,ny):
                if not visited_arr[ny][nx] and ((A[ny][nx] == A[now_y][now_x]) or (exit_map[now_y][now_x] and A[ny][nx]!=0)):
                    q.append([nx,ny])
                    visited_arr[ny][nx] = True
                    if max_y < ny:
                        max_y = ny
    return max_y
def reset_map():
    for i in range(r+3):
        for j in range(c):
            A[i][j] = 0
            exit_map[i][j] = 0
def block_move(c_, d, k):
    # check whether move down
    y = 0
    while y<=r:
        if down(c_, y):
            y +=1
        elif c_>1 and left(c_,y) and down(c_-1, y):
            c_ -=1
            y +=1
            d = (d+3)%4
        elif c_< c-2 and right(c_,y) and down(c_+1, y):
            c_ +=1
            y+=1
            d = (d+1)%4
        else: break
    if y >=4:
        A[y][c_] = k
        A[y][c_-1] = k
        A[y+1][c_] = k
        A[y-1][c_]= k
        A[y][c_+1] = k
        exit_map[y+dy[d]][c_+dx[d]] = 1
        score_ = score_cal(c_,y)-2
    else:
        score_ = 0 
        reset_map()
    return score_

score = 0
def print_mat(graph):
    for i in range(len(graph)):
        print(graph[i])
for kk in range(k):
    score += block_move(arr[kk][0]-1,arr[kk][1],kk+1)  
print(score)