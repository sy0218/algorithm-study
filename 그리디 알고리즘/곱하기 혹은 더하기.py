def solution(str):
    #첫 번재 문자를 숫자로 변경하여 대입
    answer = int(str[0])
    for i in range(1,len(str)):
        num = int(str[i])
        #두 수 중에서 하나라도 0,1 인경우 더하기수행 아니면 곱하기
        if num <= 1 or answer <=1 :
            answer += num
        else:
            answer *= num
    print(answer)
solution('02984')