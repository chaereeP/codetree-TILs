from collections import deque
import copy
k, m = map(int, input().split())
graph = []
for _ in range(5):
    graph.append(list(map(int, input().split())))
queue=deque()
for t in list(map(int, input().split())):
    queue.append(t)
# 회전
def rot_graph(graph__, tar, deg):
    graph_ = copy.deepcopy(graph__)
    dx = [-1, 0, 1, 1, 1, 0, -1, -1]
    dy = [-1, -1, -1, 0, 1, 1, 1, 0]
    data_arr=[0]*8
    for i in range(8):
        data_arr[i] = graph_[tar[1]+dy[i]][tar[0]+dx[i]]
    if deg == 90:
        id = 6
    elif deg == 180:
        id = 4
    elif deg == 270:
        id = 2
    for i in range(8):
        graph_[tar[1]+dy[i]][tar[0]+dx[i]] = data_arr[ (i+id)%8]
    return graph_
def in_range(x, y):
    return 0 <=y<5 and 0<=x<5
# score 계산하는 함수
dx = [0,0,1,-1]
dy = [1,-1,0,0]

def fill(que, grph):
    for i in range(5):
        for j in reversed(range(5)):
            if not grph[j][i]:
                grph[j][i] = que.popleft()
    return que, grph
def score_cal(rotated_graph):
    visited=[[False] *5 for _ in range(5)]
    total = 0
    tmp_graph = copy.deepcopy(rotated_graph)
    for y in range(5):
        for x in range(5):
            if not visited[y][x]:
                q, tmp = deque([(y,x)]), deque([(y,x)])
                visited[y][x] = True
                while q:
                    cur_y, cur_x = q.popleft()
                    for k in range(4):
                        new_y, new_x = cur_y+dy[k], cur_x+dx[k]
                        if in_range(new_y, new_x) and not visited[new_y][new_x] and tmp_graph[cur_y][cur_x] == tmp_graph[new_y][new_x]:
                            tmp.append((new_y, new_x))
                            visited[new_y][new_x] = True
                            q.append((new_y, new_x))
                if len(tmp) >= 3 :
                    total += len(tmp)
                    while tmp:
                        t = tmp.popleft()
                        tmp_graph[t[0]][t[1]] = 0
    return total, tmp_graph
def print_mat(graph):
    for i in range(5):
        print(graph[i])

for _ in range(k):
    max_score = 0
    max_graph = 0
    for nu in range(1,4):
        for i in range(1,4):
            for j in range(1,4):
                rotated_graph = rot_graph(graph, [j,i], 90*nu)
                cur_score, tmp_graph = score_cal(rotated_graph)
                if (cur_score > max_score):
                    max_score = cur_score
                    max_graph = tmp_graph
    if max_score ==0:
        break
    graph = max_graph
    while True:
        queue, graph = fill(queue,graph)
        new_score, graph = score_cal(graph)
        if new_score == 0:
            break
        max_score += new_score
    print(max_score)