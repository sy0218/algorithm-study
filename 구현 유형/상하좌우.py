#<문제> 여행가A는 n*n크기의 정사각형 공간 위에 서 있습니다.
# 이 공간은 1*1 크기의 정사각형으로 나누어져 있습니다.
# 가장 왼쪽 위 좌표는(1,1) 가장 오른쪽 아래 좌표는(n,n)
#상,하,좌,우 로 이동가능하며 시작은 (1,1)
#계획서를 보고 여행가를 이동시켜라
#l:왼쪽으로 한칸
#r:오른쪽으로 한칸
#u:위로 한칸
#d:아래로 한칸
def solution(n,move_plan):
    #초기값(1,1)
    x,y = 1,1

    #l,r,u,d 에 따른 이동 방향
    dx=[0,0,-1,1]
    dy=[-1,1,0,0]
    move = ['l','r','u','d'] 

    #이동 계획을 하나씩 확인하기
    for i in move_plan:
        #공간을 벗어나면 컨티튜
        if x+dx[move.index(i)]<1 or y+dy[move.index(i)]<1 or x+dx[move.index(i)]>n or y+dy[move.index(i)]>n:
            continue

        #그렇지 않으면 이동시켜주기
        else:
            x += dx[move.index(i)]
            y += dy[move.index(i)]
        print(x,y)
        
    #최종값 리턴
    return [x,y]
print(solution(5, ['r','r','r','u','d','d']))
