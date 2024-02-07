def merge_sort(input_array):
    if len(input_array) <= 1:
        return input_array

    
    mid = len(input_array) // 2
    left_array = input_array[:mid]
    right_array = input_array[mid:]

    
    left_array = merge_sort(left_array)
    right_array = merge_sort(right_array)

    
    return merge(left_array, right_array)

def merge(left, right):
    merged_array = []
    i = j = 0

    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged_array.append(left[i])
            i += 1
        else:
            merged_array.append(right[j])
            j += 1

    
    merged_array.extend(left[i:])
    merged_array.extend(right[j:])
    
    return merged_array


input_array = [5, 2, 4, 7, 1, 3, 2, 6]


sorted_array = merge_sort(input_array)

print("Given Array:", input_array )
print("Sorted Array:", sorted_array)
