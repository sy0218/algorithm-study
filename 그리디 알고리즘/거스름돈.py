def solution(n):
    count = 0
    coin = [500,100,50,10]
    for i in coin:
        count += n//i
        n = n%i
    return count

print(solution(1260))