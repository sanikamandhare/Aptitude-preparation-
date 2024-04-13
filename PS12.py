# Merge sort

def merge_sort(Array):
    if len(Array) <= 1:
        return Array

    mid = len(Array) // 2
    left_half = Array[:mid]
    right_half = Array[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)

def merge(left, right):
    merged = []
    left_index, right_index = 0, 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
        
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])

    return merged

Array = input("Enter elements separated by space: ").split()
sorted_array = merge_sort(Array)
print("Sorted array:", sorted_array)
