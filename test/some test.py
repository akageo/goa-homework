def find_smallest_int(arr):
    smallest = arr[0]
    for element in arr[1:]:
        if element < smallest:
            smallest = element
    return smallest

print(find_smallest_int([34, 15, 88, 2]))