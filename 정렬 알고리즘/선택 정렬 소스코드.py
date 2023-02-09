array = [7,5,9,0,3,1,6,2,4,8]
for i in range(len(array)):
    min_index = i
    for j in range(i+1,len(array)):
        if array[min_index] > array[j]:
            #array[min_index]보다 작게되면 최소인덱스로 저장
            min_index = j
    
    #스와프        
    array[i], array[min_index] = array[min_index], array[i]

print(array)
