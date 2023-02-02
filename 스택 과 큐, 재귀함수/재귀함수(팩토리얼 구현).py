#반복적으로 구현한 팩토리렁
def solution1(n):
    answer = 1
    for i in range(1, n+1):
        answer *= i
    return answer
print(solution1(5))

#재귀적으로 구현한 팩토리얼
def solution2(n):
    if n<=1:
        return 1
    return n*solution2(n-1)
print(solution2(5))