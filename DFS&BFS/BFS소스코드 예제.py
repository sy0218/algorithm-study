from collections import deque

def bfs(graph, start, visted):
    #큐 구현을 웨해 deque 라이브러리 사용
    queue = deque([start])
    #현재 노드를 방문 처리
    visted[start] = True
    #큐가 빌 떄 까지 반복
    while queue:
        #큐에서 하나의 원소를 뽑아 출력하기
        v = queue.popleft()
        print(v, end='')
        #아직 방문하지 않은 인접한 원소들을 큐에 삽입
        for i in graph[v]:
            if not visted[i]:
                queue.append(i)
                visted[i] = True
graph = [[]
        ,[2,3,8]
        ,[1,7]
        ,[1,4,5]
        ,[3,5]
        ,[3,4]
        ,[7]
        ,[2,6,8]
        ,[1,7]]

visited = [False]*9

print(bfs(graph,1,visited))

