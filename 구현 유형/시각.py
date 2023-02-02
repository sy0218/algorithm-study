#<문제> 정수N이 입력되면 00시 00분 00초 부터
# N시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는
#모든 경우의 수를 구하는 프로그램을 작성하세요
def solution(n):
    count = 0
    #(초,분,시)
    second = 0
    minute = 0
    hour = 0
    #hour이 n보다 작거나 같을떄 까지 반복!!(n보다 커질시 멈춤)
    while hour <= n:
        #1초씩 늘어남
        second += 1

        #만약 초가 59초가 넘어가면 0초로 초기화 하며 1분씩 늘어남
        if second > 59:
            second = 0
            minute += 1
            #59분이 넘어가면 0분을 초기화하고 한시간씩 늘어남
            if minute > 59:
                minute = 0
                hour += 1
        
        #현재 시간
        time = f'{hour}시{minute}분{second}초'
        
        #현재시간에 3이 포함되면 카운트
        if '3' in time:
            count += 1
    return count
print(solution(5))

#또 다른 방법
def solution1(n):
    count = 0
    #i는 시간, j는 분, k는 초 를  의미
    for i in range(n+1):
        for j in range(60):
            for k in range(60):
                if '3' in str(i)+str(j)+str(k):
                    count += 1
    return count
print(solution1(5))