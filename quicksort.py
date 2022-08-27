def merge_s(arr):
    def sor(low, high):
        if high - low < 2:
            return
        mid = (low + high) // 2
        sor(low, mid)
        sor(mid, high)
        merge(low, mid, high)

    def merge(low, mid, high):
        temp = []
        l, h = low, mid

        while l < mid and h < high:
            if arr[l] < arr[h]:
                temp.append(arr[l])
                l += 1
            else:
                temp.append(arr[h])
                h += 1

        while l < mid:
            temp.append(arr[l])
            l += 1
        while h < high:
            temp.append(arr[h])
            h += 1

        for i in range(low, high):
            arr[i] = temp[i - low]

    return sor(0, len(arr))

n = int(input())
arr = list(map(int, input().split()))
merge_s(arr)
for i in arr :
  print(i, end =" ")