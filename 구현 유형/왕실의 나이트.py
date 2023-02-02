#<문제> 왕실정원은 8*8좌표평면 입니다, 정원 특정 한칸에
#나이트가 서있습니다 나이트는 2가지 경우로 이동 가능합니다
#1.수평으로 두 칸 이동후 수직으로 한 칸 이동
#2.수직으로 두 칸 이동후 수평으로 한 칸 이동

#8*8 좌표평면상 나이트 위치가 주어졌을 떄 나이트가
#이동할 수 있는 경우의 수를 출력하는 프로그램 작성
#행 위치는 1~8 로 표현, 열 위치는 a~h로 표현
def solution(position):
    count = 0
    row = ['1','2','3','4','5','6','7','8']
    col = ['a','b','c','d','e','f','g','h']
    x,y = row.index(position[1]),col.index(position[0])
    #print((x,y))

    move1 = [x+1, y-2]
    move2 = [x+2, y-1]
    move3 = [x+2, y+1]
    move4 = [x+1, y+2]
    move5 = [x-1, y+2]
    move6 = [x-2, y+1]
    move7 = [x-2, y-1]
    move8 = [x-1, y-2]

    move_list = [move1, move2, move3, move4, move5, move6, move7, move8]
    
    for i in move_list:
        if i[0]>=0 and i[1]>=0 and i[0]<=8 and i[1]<=8:
            count += 1
        else:
            continue 
    
    print(count)
    return count
solution('c2')


