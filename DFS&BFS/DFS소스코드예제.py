#dfs메서드 정의
def dfs(graph, v, visted):
    #현재 노드를 방문처리
    visted[v] = True
    print(v, end='')

    #현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visted[i]:
            dfs(graph, i, visted)

graph=[[],[2,3,8],[1,7],[1,4,5],[3,5],[3,4],[7],[2,6,8],[1,7]]
visted = [False]*9
print(dfs(graph, 1, visted))

