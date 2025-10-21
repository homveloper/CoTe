def solution(arr):
    arr.sort()
    return arr

# 버블 정렬 솔루션
def bubble_solution(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# 선택 정렬 솔루션
def selection_solution(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# 음 다른 정렬 알고리즘은?
# 퀵 정렬, 병합 정렬 등등...

# 정렬 알고리즘을 직접 구현하라고 하는 경우는 잘 없다 그렇다면 왜 배우고, 그것으로 무엇을 익혀야하는가?
# 1. 정렬 알고리즘의 시간복잡도와 공간복잡도를 이해한다.
# 2. 정렬 알고리즘의 특성을 이해하여, 상황에 맞는 정렬 알고리즘을 선택할 수 있다.
# 3. 코딩 인터뷰에서 자주 출제되는 주제이므로, 면접 준비에 도움이 된다.

# 결론적으로 정렬 알고리즘을 직접 구현하는 능력보다는, 정렬 알고리즘의 특성과 성능을 이해하는 것이 더 중요하다.
# 그렇다면 평소에도 잘 익혀둬야 하는 정렬 알고리즘은 무엇일까?

# 1. 퀵 정렬 (Quick Sort)
# 2. 병합 정렬 (Merge Sort)
# 3. 힙 정렬 (Heap Sort)
# 4. 기본 정렬 함수 (예: Python의 Timsort)

# 이러한 정렬 알고리즘들의 원리와 시간복잡도, 공간복잡도를 이해하는 것이 중요하다.
# 또한, 파이썬의 기본 정렬 함수인 sort()와 sorted()가 어떻게 동작하는지도 이해하는 것이 좋다.


# 1. 퀵 정렬 (Quick Sort)
#    - 평균 시간복잡도: O(n log n)
#    - 최악 시간복잡도: O(n^2)
#    - 공간복잡도: O(log n) (재귀 호출 스택)
#    - 특징: 분할 정복 알고리즘, 평균적으로 매우 빠름, 불안정 정렬

# 2. 병합 정렬 (Merge Sort)
#    - 시간복잡도: O(n log n)
#    - 공간복잡도: O(n)
#    - 특징: 분할 정복 알고리즘, 안정 정렬, 큰 데이터셋에 적합

# 3. 힙 정렬 (Heap Sort)
#    - 시간복잡도: O(n log n)
#    - 공간복잡도: O(1)
#    - 특징: 힙 자료구조를 이용한 정렬, 불안정 정렬