def find_idx(array, start, end):
    mid = (start + end) // 2
    if array[mid] == mid:
        return mid
    if array[mid] < mid:
        return find_idx(array, mid + 1, end)
    if array[mid] > mid:
        return find_idx(array, start, mid - 1)
    raise Exception("no magic index")

print(find_idx([-40, -20, -1, 1, 2, 3, 5, 7, 9, 12, 13], 0, 9)) #7