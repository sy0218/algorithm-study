#<문제> 곱하기 혹은 더하기
#각 자리가(0~9)로만 이루어진 문자열 S가 주어졌을 떄, 왼쪽 부터
#하나씩 모든 숫자를 확인하며 x,+연산자를 넣어 결과적으로 
#가장 큰 수를 구하는 프로그램을 작성하시오
def soulution(S):
    #우선 첫번쨰 수를 문자열의 첫번쨰수로 두고
    answer = int(S[0])
    #반복문 1부터 문자열 길이만큼
    for i in range(1,len(S)):
        #number변수 를 문자열[i]로 int형태로 받아옴
        number = int(S[i])
        #number또는 answer이 1보다 작으면 더하고 아니면 곱하기 연산
        if number <= 1 or answer <=1:
            answer+=number
        else:
            answer*=number
    #최종적으로 576이라는 숫자가 나온다
    print(answer)
soulution('02984')