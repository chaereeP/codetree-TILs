k, m = map(int, input().split())
graph = []
for _ in range(5):
    graph.append(list(map(int, input().split())))
arr=[list(map(int, input().split()))]

# 회전
def rot_graph(graph, tar, deg):
    dx = [-1, 0, 1, 1, 1, 0, -1, -1]
    dy = [-1, -1, -1, 0, 1, 1, 1, 0]
    data_arr=[0]*8
    for i in range(8):
        data_arr[i] = graph[tar[0]+dx[i]][tar[1]+dy[i]]
    if deg == 90:
        id = 6
    elif deg == 180:
        id = 4
    elif deg == 270:
        id = 2
    for i in range(8):
        graph[tar[0]+dx[i]][tar[1]+dy[i]] = data_arr[ (i+id)%8]
    return graph

global idx = 0
visited = [[0]*5 for _ in range(5)]
# dfs 유물조각 개수 확인
def dfs(x,y, visited):
    # 인덱스 넘어가면 실패
    if x <0 or y<0 or x >=5 or y>=5:
        return False
    # 같은지 확인
    if not visited[x][y]:
        visited[x][y]= True
        global idx
        idx +=1
        if graph[x-1][y] == graph[x][y]:
            dfs(x-1, y, visited)
        if graph[x][y-1] == graph[x][y]:
            dfs(x, y-1, visited)
        if graph[x+1][y] == graph[x][y]:
            dfs(x+1, y, visited)
        if graph[x][y+1] == graph[x][y]:
            dfs(x, y+1, visited)
    return False

for i in range(5):
    for j in range(5):
        global idx
        idx = 0
        dfs(i,j, visited)