def mergeSort(nums):
    if len(nums) < 2:
        return nums
    mid = len(nums) // 2
    left = mergeSort(nums[:mid])
    right = mergeSort(nums[mid:])
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    if left:
        result += left
    if right:
        result += right
    return result

data = [1, 4, 2, 3.6, -1, 0, 25, -34, 8, 9, 1, 0]
print('排序前: {}'.format(data))
print('排序後: {}'.format(mergeSort(data)))