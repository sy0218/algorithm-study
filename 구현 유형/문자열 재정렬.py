#<문제> 알파벳 대문자와 숫자로만 구성된 문자열이 입력으로 주어짐
#이떄 모든 알파벳을 오름차순으로 정렬후 출력한뒤
#그 뒤에 모든 숫자를 더한 값을 이어 출력해라
 
def solution(char):
    answer = ''
    string = []
    number = 0

    for i in char:
        #i.isdigit는 모든 문자가 숫자이면 True값을 반환
        if i.isdigit() == True:
            number += int(i)

        else:
            string.append(i)
    #문자만 모은 리스트 sort로 정렬
    string.sort()

    #정렬한 리스트를 다시 문자로 만든후 더한 숫자를 붙임
    #공백없이!!
    answer = ''.join(string) + str(number)
    return answer

print(solution('K1KA5CB7'))


