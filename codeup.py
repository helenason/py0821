def heapify(uns, index, heap_size):
    largest = index
    left_index = 2 * index + 1
    right_index = 2 * index + 2
    if left_index < heap_size and uns[left_index] > uns[largest]:
        largest = left_index
    if right_index < heap_size and uns[right_index] > uns[largest]:
        largest = right_index
    if largest != index: # if changed
        uns[largest], uns[index] = uns[index], uns[largest]
        heapify(uns, largest, heap_size)

def heap(uns):
    n = len(uns)
    for i in range(n // 2 - 1, -1, -1):
        heapify(uns, i, n)
    for i in range(n - 1, 0, -1):
        uns[0], uns[i] = uns[i], uns[0]
        heapify(uns, 0, i)
    return uns

n = int(input())
arr = list(map(int, input().split()))
heap(arr)
for i in arr :
  print(i, end =" ")