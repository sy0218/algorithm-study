#1. n에서 1을 뺍니다
#2. n에서 k로 나눕니다
def solution(n, k):
    count = 0
    while True:
        #n이 k로 나누어 떨어지는 수가 될 떄까지 뺴기
        target = (n//k)*k
        count += (n-target)
        n = target

        #n이 k보다 작을떄(더이상 못나누면) 반복분 탈출
        if n < k:
            break

        #k로 나누기
        n = n//k
        count +=1
        #print(n)
    
    count += n-1
    return count
print(solution(25,5))
