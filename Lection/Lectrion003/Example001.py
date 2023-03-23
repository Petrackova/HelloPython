# Быстрая сортировка

def quick_sort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
    less = [i for i in array[1:] if i <= pivot]
    greater = [i for i in array[1:] if i > pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)


print(quick_sort([14,5,77,345,234,1,34,34,21,15]))


# Сортировка слиянием 

def merge_sort(nums):
    if len(nums) > 1:
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            nums[k] = left[i]
            i +=1
            k += 1
        while j < len(right):
            nums[k] = right[j]
            j +=1
            k += 1

list1 = [1,4,6,5,2,7,4,7,32,23,1,12,5]
merge_sort(list1)
print(list1)

