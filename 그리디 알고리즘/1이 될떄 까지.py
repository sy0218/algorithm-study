# <문제> 1이 될때까지
#어떤 수 N이 1이 될떄 까지 다음의 두 과정 중 하나를 반복적으로
#선택하여 수행하려고 합니다 단. 두번쨰는 N이 K로 나누어 떨어질 떄만 선택 가능
# 1.N에서 1을 뺍니다.
# 2.N에서 K로 나눕니다.
def solution(n,k):
    answer = 0
    #반복문 n이 1이 될떄까지
    while n != 1:
        #나누어 떨어지면 나누기
        if n%k == 0:
            n=n//k
            answer+=1
        #나누어 떨지지 않으면 n은 나누어 떨어지는수
        #그리고 n-((n//k)*4)을 해줌으로써 한번에 카운트
        else:
            num = (n//k)*k
            answer += n-num
            n = num
    print(answer)
solution(27,4)