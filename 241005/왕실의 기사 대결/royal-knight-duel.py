l, n, q = map(int, input().split())
A = []
for _ in range(l):
    A.append(list(map(int, input().split())))
knight_map = [[0]*l for _ in range(l)]
knights = []
for _ in range(n):
    knights.append(list(map(int, input().split()))) #r,c,h,w,k
    knights[-1].append(knights[-1][-1])
order_arr = []
for _ in range(q):
    order_arr.append(list(map(int, input().split())))
dx = [0,1,0,-1]
dy = [-1,0, 1, 0]

# draw initial map
import copy
def update_map(idx, knight_map_, knights_):
    collapsed=[]
    num = idx
    for i in range(l):
        for j in range(l):
            if knight_map_[i][j] == num+1:
                knight_map_[i][j]=0
    r,c,h,w,k,c_k = knights_[num]
    for hi in range(h):
        for wi in range(w):
            if knight_map_[hi + r-1][wi + c-1]!=0:
                collapsed.append(knight_map_[hi + r-1][wi + c-1])
            knight_map_[hi + r-1][wi + c-1] = num+1
    return collapsed, knight_map_

def inRange(x,y):
    return 0<=x<l and 0<=y<l

def can_move(ci, d, knights_):
    r,c,h,w,_, _ = knights_[ci-1]
    if d ==0:
        for ii in range(w):
            if not inRange(r-1-1,c-1+ii) or A[r-1-1][c-1+ii] == 2:
                return False
    if d ==1:
        for ii in range(h):
            if not inRange(r-1+ii,c-1+w) or A[r-1+ii][c-1+w] == 2:
                return False   
    if d ==2:
        for ii in range(w):
            if not inRange(r-1+h,c-1+ii) or A[r-1+h][c-1+ii] == 2:
                return False
    if d ==3:
        for ii in range(h):
            if not inRange(r-1+ii,c-1-1) or A[r-1+ii][c-1-1] == 2:
                return False
    return True   
from collections import deque
def cal_damage(moved, knight_map_, knights_):
    for i in range(l):
        for j in range(l):
            if A[i][j] ==1 and knight_map_[i][j] in moved:
                knights_[i-1][-1] -=1
    for ii in moved:
        i = ii-1
        if knights_[i][-1]<=0:
            r,c,h,w,_, _ = knights_[i]
            for hi in range(h):
                for wi in range(w):
                    if knight_map_[hi + r-1][wi + c-1]==i+1:
                        knight_map_[hi + r-1][wi + c-1] = 0
# move
for i in range(len(knights)):
    update_map(i, knight_map, knights)
for or_idx in range(len(order_arr)):
    i, d = order_arr[or_idx]
    # check whether knight alive
    if knights[i-1][-1] > 0:
        tmp_knight_map = copy.deepcopy(knight_map)
        tmp_knights = copy.deepcopy(knights)
        que = deque(([i]))
        sw = 1
        moved_arr = []
        visited = [0]*len(knights)
        visited[i-1] = True
        while que and sw:
            cur_i = que.popleft()
            if can_move(cur_i,d, tmp_knights):
                # print(cur_i,can_move(cur_i,d, tmp_knights), tmp_knights)
                tmp_knights[cur_i-1][0] += dy[d]
                tmp_knights[cur_i-1][1] += dx[d]
                collapsed, tmp_knight_map = update_map(cur_i-1, tmp_knight_map,tmp_knights)
                while collapsed:
                    t=collapsed.pop()
                    if not visited[t-1]:
                        que.append(t)
                        visited[t-1] = True
                        moved_arr.append(t)
            else: 
                sw = 0
        if sw :
            # print('mo',moved_arr)
            cal_damage(moved_arr, tmp_knight_map, tmp_knights)
            knight_map, knights = tmp_knight_map, tmp_knights

#calculate score
score = 0
for i in range(len(knights)):
    if knights[i][-1] > 0:
        score += (knights[i][-2]- knights[i][-1])
# print_map(knight_map)
print(score)