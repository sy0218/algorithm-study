#입력
n,k = map(int, input().split())
'''
array_a = list(map(int,input().split()))
array_b = list(map(int,input().split()))

print(array_a)
'''

array_a = []
array_b = []
for i in range(n):
    array_a.append(int(input('a배열 입력:')))
    array_b.append(int(input('b배열 입력:')))



def solution(n, k, array_a, array_b):
    array_a.sort()
    array_b.sort(reverse = True)#내림차순 정렬 수행

    for i in range(k):
        if array_a[i] < array_b[i]:
            array_a[i],array_b[i] = array_b[i],array_a[i]

    return sum(array_a)   

print(solution(n,k,array_a,array_b))



