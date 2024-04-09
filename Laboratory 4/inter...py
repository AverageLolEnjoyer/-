def interpolation_search(lst, search_item):
    low = 0
    high = len(lst) - 1
    search_res = False

    while (low <= high and search_item >= lst[low]) and search_item <= lst[high] and not search_res:

        middle = low + int(((high - low) / (lst[high] - lst[low])) * (search_item - lst[low]))
        guess = lst[middle]
        if guess == search_item:
            search_res = True
        if guess < search_item:
            low = middle + 1
        else:
            high = middle - 1
    return search_res, middle


lst = [3, 5, 11, 12, 15, 23, 25, 34, 67, 86]
value = 67

result, index = interpolation_search(lst, value)

if result:
    print(f"Элемент найден! На индексе {index}")
else:
    print("Элемент не найден!")

print(f"Последовательность {lst}")
print(f"Элемент {value}")
