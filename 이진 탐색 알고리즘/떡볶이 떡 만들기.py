result = 0

def solution(array,m):
    #이진 탐색을 위한 시작점과 끝점 설정
    start = 0
    end  = max(array)

    #이진탐색 수행(반복적)
    
    while(start<=end):
        total = 0
        mid = (start+end)//2
        
        #잘랐을떄 떡의 양 계산하기
        for i in array:
            if i > mid:
                total += i-mid
        
    if total < m:
        end = mid-1
    else:
        result = mid
        start = mid + 1


solution([19,15,10,17],6)
print(result)