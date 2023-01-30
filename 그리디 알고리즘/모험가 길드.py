#<문제> 모험가 길드
#마을에 모험가 N명이 있습니다. 공포도가 X인 모험가는 반드시
#X명 이상으로 구성된 모험가 그룹에 참여해야 합니다
#N명의 모험가에 대한 정보가 주어졌을떄, 
#여행을 떠나는 그룹의 최댓값을 구하시오
def solution(N,K):
    #총 그릅의 수
    answer = 0
    #현재 그룹의 인원수
    now_answer = 0
    #먼저 모험가 공포도기준 오름차순으로 정렬
    K.sort()
    
    for i in K:
        now_answer += 1
        #만약 i가 현재 그룹의 수와 같거나 작다면 그룹을 구성한다
        if i <= now_answer:
            answer += 1
            now_answer = 0

    print(answer)
solution(5,[2,3,1,2,2])