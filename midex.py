

## **1. Linear Search using Divide and Conquer**


def linear_search_dc(arr, low, high, key):
    if low > high:
        return -1
    if low == high:
        if arr[low] == key:
            return low
        else:
            return -1
    mid = (low + high) // 2
    left = linear_search_dc(arr, low, mid, key)
    if left != -1:
        return left
    return linear_search_dc(arr, mid + 1, high, key)

arr = list(map(int, input().split()))
key = int(input())

result = linear_search_dc(arr, 0, len(arr) - 1, key)

if result != -1:
    print("Element found at position", result)
else:
    print("Element not found")
```

---

## **2. Binary Search using Divide and Conquer**


def binary_search_dc(arr, low, high, key):
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == key:
        return mid
    elif key < arr[mid]:
        return binary_search_dc(arr, low, mid - 1, key)
    else:
        return binary_search_dc(arr, mid + 1, high, key)

arr = list(map(int, input().split()))
key = int(input())

result = binary_search_dc(arr, 0, len(arr) - 1, key)

if result != -1:
    print("Element found at position", result)
else:
    print("Element not found")
```

---

## **3. Towers of Hanoi**


def towers_of_hanoi(n, source, auxiliary, destination):
    if n == 1:
        print("Move disk 1 from", source, "to", destination)
        return
    towers_of_hanoi(n - 1, source, destination, auxiliary)
    print("Move disk", n, "from", source, "to", destination)
    towers_of_hanoi(n - 1, auxiliary, source, destination)

n = int(input())
towers_of_hanoi(n, "A", "B", "C")
```

---

## **4. Selection Sort**

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

arr = list(map(int, input().split()))
print(selection_sort(arr))
```

---

## **5. Quick Sort**


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)

arr = list(map(int, input().split()))
print(quick_sort(arr))
```

---

## **6. Merge Sort**


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

arr = list(map(int, input().split()))
merge_sort(arr)
print(arr)
```

---

## **7. Prim’s Algorithm**


INF = 9999999

n = int(input())
graph = []

for i in range(n):
    graph.append(list(map(int, input().split())))

selected = [False] * n
selected[0] = True
edges = 0
cost = 0

while edges < n - 1:
    minimum = INF
    x = 0
    y = 0
    for i in range(n):
        if selected[i]:
            for j in range(n):
                if not selected[j] and graph[i][j] != 0:
                    if graph[i][j] < minimum:
                        minimum = graph[i][j]
                        x = i
                        y = j
    print(x, "-", y, ":", graph[x][y])
    cost += graph[x][y]
    selected[y] = True
    edges += 1

print("Total cost:", cost)
```

