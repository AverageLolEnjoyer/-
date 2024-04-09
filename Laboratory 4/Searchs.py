import random
def binary_search(arr, target):
    first = 0
    last = len(arr) - 1

    while first <= last:
        middle = (first + last) // 2

        if arr[middle] == target:
            return middle
        elif arr[middle] < target:
            first = middle + 1
        else:
            last = middle - 1

    return -1

def insert_element(arr, element):
    index = binary_search(arr, element)
    if index == -1:
        arr.append(element)
        arr.sort()
        return True
    else:
        return False

def delete_element(arr, element):
    index = binary_search(arr, element)
    if index != -1:
        arr.pop(index)
        return True
    else:
        return False

arr = [random.randint(1, 100) for _ in range(20)]
arr.sort()
target = arr[random.randint(0,19)]

print(arr)
print(target)
print(binary_search(arr, target))

