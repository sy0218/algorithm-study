#먼저 들어온 데이터가 나중에 나가는 형식의 자료구조(선입후출)

#<스택 구현 예제>
stack= []
stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop() #맨뒤의 7삭제
stack.append(1)
stack.append(4)
stack.pop()#맨뒤의 4삭제

print(stack)
print(stack[::-1])#최상단 원소부터 출력