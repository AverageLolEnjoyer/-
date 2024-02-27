import time
import random
import copy
import heapq

#создание матрицы
def gen_random(m, n, min_limit, max_limit):
    matrix = []
    for i in range(m):
        row = []
        for j in range(n):
            row.append(random.randint(min_limit, max_limit))
        matrix.append(row)
    return matrix

n =                             int(input())
m =                             int(input())
min_t =                           int(input())
max_t =                           int(input())

arr = gen_random(n, m, min_t, max_t)
arr_2 = arr # создание дополнительной матрицы для высчитывания времени со стандартной сортировкой
n = len(arr)

#Стандартная сортировка
start_time_st = time.time()
arr_2.sort()
print("Стандартная сортировка--- {0} ms ---".format(round((time.time() - start_time_st)*1000)))


#Сортировка вставкой
start_time = time.time()
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

for i in range(n):
    arr[i] = insertion_sort(arr[i])
print("Сортировка вставкой--- {0} ms ---".format(round((time.time() - start_time)*1000)))

#Сортировка выбором
start_time = time.time()
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

for i in range(n):
    arr[i] = selection_sort(arr[i])

print("Сортировка выбором--- {0} ms ---".format(round((time.time() - start_time)*1000)))


#Быстрая сортировка
start_time = time.time()
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)


for i in range(n):
    arr[i] = quicksort(arr[i])

print("Быстрая сортировка--- {0} ms ---".format(round((time.time() - start_time)*1000)))


#Сортировка пузырьком
start_time = time.time()
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

for i in range(n):
    arr[i] = bubble_sort(arr[i])

print("Сортировка пузырьком--- {0} ms ---".format(round((time.time() - start_time)*1000)))

#Сортировка Шелла
start_time = time.time()
def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    return arr

for i in range(n):
    arr[i] = shell_sort(arr[i])

print("Сортировка Шелла--- {0} ms ---".format(round((time.time() - start_time)*1000)))

#Турнирная сортировка
start_time = time.time()
def tournament_sort(array):
    MAX_SIZE = len(array)
    size = len(array)
    pq = []
    for _ in range(MAX_SIZE):
        heapq.heappush(pq, array.pop(0))
    winners = []
    losers = []

    while array:
        if not winners:
            winners.append(pq[0])
            heapq.heappop(pq)

        if array[0] > winners[-1]:
            heapq.heappush(pq, array.pop(0))
        else:
            losers.append(array.pop(0))

        if pq:
            winners.append(pq[0])
            heapq.heappop(pq)

    while pq:
        winners.append(pq[0])
        heapq.heappop(pq)

    if not losers:
        return winners

    array = losers + winners
    while len(array) > size:
        array.pop()

    return tournament_sort(array)

for i in range(n):
    arr[i] = tournament_sort(arr[i])

print("Турнирная сортировка"
      "--- {0} ms ---".format(round((time.time() - start_time)*1000)))
