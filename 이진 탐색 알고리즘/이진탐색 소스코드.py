#이진탐색
def binary_search(array, target, start, end):
    if start > end or target not in array:
        return None
    #중간값
    mid  = (start+end)//2
    #print(array[mid])
    #print(target)
    #찾은 경우 중간값 인덱스 반환
    if array[mid] == target:
        return mid
    
    #중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽확인
    elif array[mid] > target:
        return binary_search(array,target,start,mid-1)
    
    elif array[mid] < target:
        return binary_search(array,target, mid+1, end)

print(binary_search([1,3,5,7,9,11,13,15,17,19],4,0,9))