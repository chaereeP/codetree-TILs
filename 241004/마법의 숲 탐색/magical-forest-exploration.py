# input
r, c, k = map(int, input().split())
arr = list()
for _ in range(k):
    arr.append(list(map(int, input().split())))

import queue
dx= [0, 1, 0, -1]
dy= [-1, 0, 1, 0]
stacked_arr, exit_arr, connected_arr = [], [], []
def occupied(x,y):
    global stacked_arr
    if not len(stacked_arr):
        return False
    for stacked in stacked_arr: # [x, y]가 stacked된 arr와 겹치는지 확인
        for i in range(4):
            if [x, y] == [stacked[0]+dx[i], stacked[1]+dy[i]]:
                return True
    return False

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

def get_connected_arr(stacked_arr, connected_arr):
    def connected(x,y,d, tar_x, tar_y):
        global dx, dy
        nx, ny = x+dx[d], y+dy[d]
        ddx=[0,1,2,1,0,-1,-2,-1]
        ddy=[-2,-1,0,1,2,1,0,-1]
        for idx in range(8):
            if tar_x+ddx[idx]== nx and  tar_y+ddy[idx]==ny:
                return True
        return False
    for kk in range(len(stacked_arr)-1):
            if connected(stacked_arr[-1][0],stacked_arr[-1][1],exit_arr[-1],stacked_arr[kk][0],stacked_arr[kk][1]):
                connected_arr[-1].append(kk)
                connected_arr[kk].append(len(stacked_arr)-1)
    return connected_arr

def score_cal(connected_arr): # bfs
    connected_arr = get_connected_arr(stacked_arr, connected_arr)
    max_y = 0
    visited_arr =[0] * len(stacked_arr)
    q = queue.Queue()
    start = len(stacked_arr)-1
    q.put(start)
    visited_arr[start] = 1
    if max_y < stacked_arr[start][1]:
        max_y = stacked_arr[start][1]
    while not q.empty():
        now = q.get()
        for next_ in connected_arr[now]:
            if not visited_arr[next_]:
                visited_arr[next_] = 1
                q.put(next_)
                if max_y < stacked_arr[next_][1]:
                    max_y = stacked_arr[next_][1]
    return max_y

def block_move(c_, d):
    score = 0 
    global stacked_arr, exit_arr,connected_arr
    # check whether move down
    y = 0
    while y<=r-1:
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
    if y >=3:
        stacked_arr.append([c_,y])
        exit_arr.append(d)
        connected_arr.append([len(stacked_arr)-1])
        if len(stacked_arr) == 1:
            score = r
        else: score = score_cal(connected_arr)
    else:
        score = 0 
        stacked_arr, exit_arr,connected_arr = [], [], []
    return score

score = 0
for kk in range(k):
    score += block_move(arr[kk][0]-1,arr[kk][1])  
print(score)