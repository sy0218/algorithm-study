array = [7,5,9,0,3,1,6,2,4,8]

for i in range(1,len(array)):
    for j in range(i,0,-1):#i부터 1까지 1씩 감소하는 반복
        #왼쪽이 더크면 스왑
        if array[j] < array[j-1]:
            array[j] , array[j-1] = array[j-1], array[j]
        #왼쪽이 더 작으면 브레이크
        else:
            break
print(array)