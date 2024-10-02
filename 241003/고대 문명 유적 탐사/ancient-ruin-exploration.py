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

# dfs 유물조각 개수 확인
def dfs(x,y, idx, num, graph):
    # 인덱스 넘어가면 실패
    if x <0 or y<0 or x >=5 or y>=5:
        return idx
    # 같은지 확인
    if graph[x][y] == num and not visited[x][y]:
        idx +=1
        dfs(x-1, y, idx, num, graph)
        dfs(x, y-1, idx, num, graph)
        dfs(x+1, y, idx, num, graph)
        dfs(x, y+1, idx, num, graph)