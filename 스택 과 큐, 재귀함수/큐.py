#큐는 먼저 들어온 데이터가 먼저 나가는(선입선출)의 자료구조
#<큐 구현 예제>
#큐를 이용할 떄는 꼭!! deque라이브러리를 사용(시간복잡도 이유)

from collections import deque

queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft() # 젤 왼쪽 5삭제
queue.append(1)
queue.append(4)
queue.popleft() # 젤 왼쪽 2삭제

print(queue)
queue.reverse()#역순으로 바꾸기
print(queue)#나중에 들어온 원소부터 출력