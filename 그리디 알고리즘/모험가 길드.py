def solution(n,data):
    data.sort()
    answer = 0 #총 그룹의수
    now_answer = 0 #현재 그룹의 수

    for i in data: #정렬 했기 떄문에 공포도 낮은 것부터 하나씩 확인
        now_answer += 1 #현재 그룹에 해당 모험가를 포함시키기
        if i <= now_answer:
            now_answer = 0
            answer += 1
    print(answer)
solution(5,[2,3,1,2,2])