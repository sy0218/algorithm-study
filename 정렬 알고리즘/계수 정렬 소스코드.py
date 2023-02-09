#모든 원소의 값이 0보다 그거나 같다고 가정
array = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]
print(array.count(0))
#모든 범위를 포함하는 리스트 선언
list = [0]*(max(array)+1)


for i in array:
    list[i] += 1

print(list)
for i in range(len(list)):
    for j in range(array.count(i)):
        print(i,end=' ')
    
