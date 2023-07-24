# write a function for bubble sorting 
def bubble(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            # if the element found is greater than the next element, swap them
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    # return the sorted array
    return arr


# write a function for selection sorting
def selection(arr):
    n = len(arr)
    for i in range(n):
        # find the minimum element in the remaining unsorted array
        min_idx = i
        for j in range(i+1, n):
            if arr[min_idx] > arr[j]:
                min_idx = j
        # swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    # return the sorted array
    return arr

# writing a function for: 1^3 + 2^3 + 3^3 + ... + n^3
def sum_of_cubes(n):
    sum = 0
    for i in range(1, n+1):
        sum += i**3
    return sum


print(sum_of_cubes(5))
