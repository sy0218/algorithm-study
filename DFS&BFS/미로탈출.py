#문제<미로탈출>
#동빈이는 n*m크기의 직사각형 형태의 미로에 갇혔습니다.
#동빈이의 위치는 (1,1)이며 미로의 출구는 (n,m)위치에 존재하며
#한칸씩 이동할수 있습니다 이떄 괴물이 있는 부분은 0
#없는 부분은 1로 표시되있습니다
#동빈이가 탈출을 위해 움직여야 하는 최소 간의 개수를 구하세요
#칸을 셀 떄는 시작 칸과 마지막 칸을 모두 포햄해 계산합니다.
from collections import deque

n,m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    
    queue = deque()
    queue.append((x,y))

    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            #공간은 벗어날경우 
            if nx<0 or ny<0 or nx>=n or ny>=m:
                continue
            #벽일경우
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y]+1
                queue.append((nx,ny))


    return graph

print(bfs(0,0))