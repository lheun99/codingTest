array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    # 가장 작은 원소의 인덱스
    min_index = i

    for j in range(i+1, len(array)):
        # 가장 작은 원소 찾기
        if array[min_index] > array[j]:
            min_index = j

    # 스와프 (두 원소의 위치를 바꾸는 파이썬 특징)
    array[i], array[min_index] = array[min_index], array[i]

print(array)
