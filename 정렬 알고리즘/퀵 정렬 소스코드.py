#퀵정렬
#1)왼쪽에서 출발해 피벗보다 큰거랑
#오른쪽에서 출발해 피벗보다 작은거 스위칭

#2)그러나 왼쪽이 오른쪽 인덱스 보다 커지면(스위칭 되면)
#오른쪽 값과 피벗값 스위칭 한후 분할 한다

array = [5,7,9,0,3,1,6,2,4,8]
def quick_sort(array, start, end):
    #원소가 한개인 경우 종료
    if start >= end:
        return
    
    pivote = start
    left = start+1
    right = end

    while left <= right:

        while left<=end and array[left]<=array[pivote]:
            left += 1
        while right>start and array[right]>=array[pivote]:
            right -= 1
        
        if left > right:
            array[pivote], array[right] = array[right],array[pivote]
        else:
            array[left],array[right] = array[right],array[left]
    
    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)

quick_sort(array,0,len(array)-1)
print(array)